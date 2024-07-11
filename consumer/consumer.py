import logging
import datetime
import json
import yaml
from kafkaService import KafkaService
from mongodbService import MongodbService
import os


def main():
    with open("/config/config.yaml", "r") as f:
        config = yaml.safe_load(f)
        timeout_try_to_connect_kafka = config["time"]["timeout_try_to_connect_kafka"]
        interval_connect_kafka = config["time"]["interval_connect_kafka"]

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    kafka_service = KafkaService(timeout_try_to_connect_kafka, interval_connect_kafka)
    kafka_service.try_create_consumer_interval()

    mongodb_service = MongodbService()

    for message in kafka_service.consumer:
        event = message.value
        event_str = event.decode("utf-8")
        json_data = json.loads(event_str)
        json_data["timestamp"] = datetime.datetime.fromisoformat(json_data["timestamp"])
        logger.info(f"Received event: {json_data}")
        mongodb_service.collection.insert_one(json_data)
        kafka_service.consumer.commit()
        logger.info(f"Event inserted to database")


if __name__ == "__main__":
    main()
