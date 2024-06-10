import pika
import json
import os
import time
from db.database import SessionLocal
from repositories.stock_repository import StockRepository
from schemes.stock_schema import StockCreate

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
connection = None
channel = None
consuming = True


def create_connection():
    global connection
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBITMQ_HOST)
            )
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Connection to RabbitMQ failed, retrying in 5 seconds... Error: {e}")
            time.sleep(5)


def callback(ch, method, properties, body):
    message = json.loads(body)
    create_stock_record(message["product_id"])
    ch.basic_ack(delivery_tag=method.delivery_tag)


def create_stock_record(product_id):
    db = SessionLocal()
    stock_repository = StockRepository(db)
    stock_data = StockCreate(product_id=product_id)
    stock_repository.create(stock_data)
    db.close()


def start_consuming():
    global channel
    connection = create_connection()
    channel = connection.channel()
    channel.queue_declare(queue="product_queue", durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="product_queue", on_message_callback=callback)
    while consuming:
        try:
            connection.process_data_events(time_limit=1)
        except Exception as e:
            print(f"Error while consuming: {e}")


def stop_consuming():
    global consuming
    consuming = False
    if connection and connection.is_open:
        connection.close()
