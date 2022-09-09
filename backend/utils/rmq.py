import json
import pika
import logging
from queue import Queue

logging.basicConfig(
    level=logging.INFO, format="[%(module)s] [%(levelname)s] %(asctime)s --  %(message)s"
)
logger = logging.getLogger(__name__)

class RMQ:
    def __init__(self, config, queue: Queue) -> None:
        
        config = config["rmq"]
        host = config["host"]
        exchange = config["exchange"]
        routing_key = config["routing_key"]
        queue_name = config["queue_name"]
        self.logs: bool = config["debug"]["logs"]
        
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        
        self.channel.exchange_declare(
			exchange=self.exchange,
			exchange_type='direct'
		)
        self.rmq_queue = self.channel.queue_declare(queue_name)
        self.channel.queue_bind(
            exchange=exchange,
            queue=queue_name,
            routing_key=routing_key
        )
        self.channel.basic_consume(self.rmq_queue, on_message_callback=self.callback)
        self.queue = queue
    
    def callback(self, ch, method, _, body):
        payload = json.loads(body.decode('utf-8'))
        self.queue.put(payload)
        if self.logs: logger.info(f"Consuming data from rabbitmq - {payload}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume(self):
        self.channel.start_consuming()
    
    def kill(self):
        self.channel.close()
        self.connection.close()