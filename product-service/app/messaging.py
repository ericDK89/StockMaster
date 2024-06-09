import pika
import json
import os

RABBITMQ_HOST: str = os.getenv("RABBITMQ_HOST", "localhost")


def send_message_to_queue(message) -> None:
    with pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST)) as conn:
        channel = conn.channel()
        channel.queue_declare(queue="product_queue", durable=True)
        channel.basic_publish(
            exchange="",
            routing_key="product_queue",
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2),
        )
