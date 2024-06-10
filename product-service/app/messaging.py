"""File to handle messaging RABBITMQ"""

import json
import os
import pika

RABBITMQ_HOST: str = os.getenv("RABBITMQ_HOST", "localhost")


def send_message_to_queue(message) -> None:
    """
    This function sends a message to a RabbitMQ queue named 'product_queue'.

    Parameters:
    message (dict): The message to be sent to the queue. It should be a dictionary that will be converted to a JSON string.

    Returns:
    None

    The function establishes a blocking connection with the RabbitMQ server, declares the queue (if it doesn't exist already),
    and publishes the message to the queue. The message is sent with a delivery mode of 2, which makes it persistent on the server.
    """
    with pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST)) as conn:
        channel = conn.channel()
        channel.queue_declare(queue="product_queue", durable=True)
        channel.basic_publish(
            exchange="",
            routing_key="product_queue",
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2),
        )
