import time
import yaml
import logging
from Event import Event
from kafka_service import KafkaService


def main():
    """
    Main function to load configuration, create KafkaService, and generate events.
    Reads config, initializes Kafka connection, and sends events in a loop.
    """
    with open("/config/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    num_of_sec_generate_event_interval = config["time"]["num_of_sec_genrate_event_interval"]
    attempt_to_connect_to_kafka_interval = config["kafka_connection"]["attempt_to_connect_to_kafka_interval"]
    event_config = config["event"]

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    kafka_service = KafkaService(attempt_to_connect_to_kafka_interval)
    kafka_service.try_to_create_producer()
    logger.info(
        f"Will generate one unique order every {num_of_sec_generate_event_interval} seconds"
    )

    while True:
        try:
            event = Event(event_config)
            logger.info(f"Sent event")
            kafka_service.send_event_to_kafka(event)
            time.sleep(num_of_sec_generate_event_interval)
        except Exception as e:
            logger.error(f"Failed to send event {e}")


if __name__ == "__main__":
    main()
