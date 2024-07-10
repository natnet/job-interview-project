import logging
import jsonpickle
import datetime
import json
from kafkaService import KafkaService
from mongodbService import MongodbService

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    kafka_service = KafkaService()
    kafka_service.try_create_consumer_interval()

    mongodb_service = MongodbService()
    
    for message in kafka_service.consumer:
        event = message.value
        event_str = event.decode('utf-8')
        json_data = json.loads(event_str)
        json_data['timestamp'] = datetime.datetime.fromisoformat(json_data['timestamp'])
        logger.info(f"Received event: {json_data}")
        mongodb_service.collection.insert_one(json_data)
        logger.info(f"Event inserted to database")
        
if __name__ == '__main__':
    main()
