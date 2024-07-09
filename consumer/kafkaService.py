import time
import six
import sys
import os
import logging
from kafka import KafkaConsumer

if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves


class KafkaService:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    def __init__(self):
        self.bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
        self.topic_name = os.getenv('TOPIC_NAME')
        self.consumer = None

    def create_consumer(self):
        try:
            consumer = KafkaConsumer(self.topic_name, bootstrap_servers=self.bootstrap_servers)
            self.logger.info("Successfully connected to Kafka.")
            return consumer
        except Exception as e:
            self.logger.error(f"Error creating KafkaConsumer: {e}")
            return None
    
    def try_create_consumer_interval(self):
        while self.consumer is None:
            self.consumer = self.create_consumer()
            if self.consumer is None:
                time.sleep(3)
                self.logger.info("Retrying connection to Kafka...")
        self.logger.info("Gonna start listening")