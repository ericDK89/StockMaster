"""File to create messaging for stock, to handle RABBITMQ"""

import json
import os
import time
import pika
from db.database import SessionLocal
from repositories.stock_repository import StockRepository
from schemes.stock_schema import StockCreate, Stock

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
connection = None
channel = None
consuming = True


def create_connection():
    """
    This function creates a connection to the RabbitMQ server.

    Returns:
    pika.BlockingConnection: The connection to the RabbitMQ server.

    If the connection fails, it will keep trying every 5 seconds until a connection is established.
    """
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


def callback(ch, method, _, body):
    """
    This function is the callback that is called when a message is consumed from the RabbitMQ queue.

    Parameters:
    ch (pika.Channel): The channel from which the message was consumed.
    method (pika.spec.Basic.Deliver): The method frame.
    properties (pika.spec.BasicProperties): The properties.
    body (bytes): The body of the message.

    The function processes the message and acknowledges it.
    """
    message = json.loads(body)
    action = message.get("action")

    if action == "delete":
        delete_stock(message["product_id"])
    else:
        create_stock_record(message["product_id"])

    ch.basic_ack(delivery_tag=method.delivery_tag)


def delete_stock(product_id: int) -> None:
    """
    This function deletes a stock record.

    Parameters:
    product_id (int): The ID of the product for which to delete the stock record.
    """
    with SessionLocal() as db:
        stock_repository = StockRepository(db)
        stock: Stock | None = stock_repository.get_stock_by_product_id(
            product_id=product_id
        )
        if stock:
            stock_repository.delete(stock=stock)


def create_stock_record(product_id) -> None:
    """
    This function creates a new stock record.

    Parameters:
    product_id (int): The ID of the product for which to create the stock record.
    """
    with SessionLocal() as db:
        stock_repository = StockRepository(db)
        stock_data = StockCreate(product_id=product_id)
        stock_repository.create(stock_data)


def start_consuming():
    """
    This function starts consuming messages from the RabbitMQ queue.

    It creates a connection and a channel, declares the queue, sets the QoS, and starts consuming messages.
    """
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
    """
    This function stops consuming messages and closes the connection to the RabbitMQ server.
    """
    global consuming
    consuming = False
    if connection and connection.is_open:
        connection.close()
