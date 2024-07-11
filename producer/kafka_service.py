import json
import os
import time
import six
import sys
import yaml
import logging
from kafka import KafkaProducer
from Event import Event

if sys.version_info >= (3, 12, 0):
    sys.modules["kafka.vendor.six.moves"] = six.moves


class KafkaService:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def __init__(self, attempt_to_connect_to_kafka_interval):
        """
        Initialize KafkaService with the connection attempt interval.
        Set bootstrap_servers and topic_name from environment variables.
        """
        self.attempt_to_connect_to_kafka_interval = attempt_to_connect_to_kafka_interval
        self.bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        self.topic_name = os.getenv("TOPIC_NAME")

    def create_producer(self):
        """
        Try to create a Kafka producer.
        Logs success or failure and returns the producer or None.
        """
        try:
            producer_attempt = KafkaProducer(bootstrap_servers=self.bootstrap_servers)
            KafkaService.logger.info("Successfully connected to Kafka.")
            return producer_attempt
        except Exception as e:
            KafkaService.logger.error(f"Error creating KafkaProducer: {e}")
            return None

    def try_to_create_producer(self):
        """
        Attempt to create a Kafka producer until successful.
        Retries after sleeping for the specified interval.
        """
        self.producer = None
        while self.producer is None:
            self.producer = self.create_producer()
            if self.producer is None:
                KafkaService.logger.info("Retrying connection to Kafka...")
                time.sleep(self.attempt_to_connect_to_kafka_interval)

    def send_event_to_kafka(self, event: Event):
        """
        Send an event to Kafka.
        Logs success or failure of the send operation.
        """
        try:
            event_dict = event.to_dict()
            self.producer.send(self.topic_name, json.dumps(event_dict).encode("utf-8"))
            KafkaService.logger.info("Event sent to Kafka successfully.")
        except Exception as e:
            KafkaService.logger.error(f"Error sending event to Kafka: {e}")
