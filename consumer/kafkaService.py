import time
import six
import sys
import os
import logging
from kafka import KafkaConsumer

if sys.version_info >= (3, 12, 0):
    sys.modules["kafka.vendor.six.moves"] = six.moves


class KafkaService:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def __init__(self, timeout_try_to_connect_kafka, interval_connect_kafka):
        """
        Initialize KafkaService with connection timeout and interval.
        Sets bootstrap_servers, topic_name, consumer, and group_id.
        """
        self.bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        self.topic_name = os.getenv("TOPIC_NAME")
        self.consumer = None
        self.group_id = os.getenv("GROUP_ID")
        self.timeout_try_to_connect_kafka = timeout_try_to_connect_kafka
        self.interval_connect_kafka = interval_connect_kafka

    def create_consumer(self):
        """
        Try to create a Kafka consumer.
        Logs success or failure and returns the consumer or None.
        """
        try:
            consumer = KafkaConsumer(
                self.topic_name,
                bootstrap_servers=self.bootstrap_servers,
                group_id=self.group_id,
                auto_offset_reset="earliest",
                enable_auto_commit=False,
            )
            self.logger.info("Successfully connected to Kafka.")
            return consumer
        except Exception as e:
            self.logger.error(f"Error creating KafkaConsumer: {e}")
            return None

    def try_create_consumer_interval(self):
        """
        Attempt to create a Kafka consumer within a timeout period.
        Retries after sleeping for the specified interval.
        """
        time_out = 0
        while self.consumer is None:
            self.consumer = self.create_consumer()
            if time_out == self.timeout_try_to_connect_kafka:
                self.logger.error(
                    f"timeout error after multiple connection attempts to kafka"
                )
                return
            if self.consumer is None:
                time_out += 1
                time.sleep(self.interval_connect_kafka)
                self.logger.info("Retrying connection to Kafka...")
        self.logger.info("Going to start listening")
