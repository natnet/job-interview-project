import time
import logging
from Event import Event
from kafka_service import KafkaService


    
def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    kafka_service = KafkaService()
    kafka_service.try_to_create_producer()
    logger.info("Will generate one unique order every 1 seconds")
    
    while True:
        try:
            event = Event()
            logger.info(f"Sent event")
            kafka_service.send_event_to_kafka(event)
            time.sleep(1)
        except Exception as e:
            logger.error(f"Failed to send event {e}")
            
if __name__ == '__main__':
    main()
    
