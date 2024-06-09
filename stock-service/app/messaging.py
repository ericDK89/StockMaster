import pika
import json
import os
import time
from db.database import SessionLocal
from repositories.stock_repository import StockRepository
from schemes.stock_schema import StockCreate

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")


def create_connection():
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
    create_stock_record(message["product_id"], message["quantity"])
    ch.basic_ack(delivery_tag=method.delivery_tag)


def create_stock_record(product_id, quantity):
    db = SessionLocal()
    stock_repository = StockRepository(db)
    stock_data = StockCreate(product_id=product_id, quantity=quantity)
    stock_repository.create(stock_data)
    db.close()


def start_consuming():
    connection = create_connection()
    channel = connection.channel()
    channel.queue_declare(queue="product_queue", durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="product_queue", on_message_callback=callback)
    channel.start_consuming()
