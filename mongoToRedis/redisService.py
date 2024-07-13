import datetime
import logging
import redis
import json
import os
from mongoService import MongoService


class RedisService:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def __init__(self):
        """
        Initialize RedisService with connection details from environment variables.
        Sets up Redis connection and retrieves max_date_event.
        Handles connection errors.
        """
        try:
            redis_port = os.getenv("REDIS_PORT")
            self.r = redis.Redis(host="redis", port=redis_port, decode_responses=True)
        except redis.ConnectionError as e:
            self.logger.error(f"Error connecting to Redis: {e}")
            raise
        
        self.max_date_event = (
            datetime.datetime.fromisoformat(self.r.get("max_date_event"))
            if self.r.get("max_date_event") is not None
            else datetime.datetime.min
        )
        self.logger.info(f"\n\nmax_date_event: {self.max_date_event}\n\n")

    def process_events(self):
        """
        Process events from MongoDB and store them in Redis.
        Updates max_date_event and logs processed events.
        """
        self.max_date_event
        mongo_service = MongoService()
        try:
            count = 0
            pipe = self.r.pipeline()
            for event in mongo_service.get_filtered_collection(self.max_date_event):
                count += 1
                if event["timestamp"] > self.max_date_event:
                    self.max_date_event = event["timestamp"]
                del event["_id"]
                event["timestamp"] = event["timestamp"].isoformat()
                pipe.set(
                    f"{event['reporter_id']}:{event['timestamp']}", json.dumps(event)
                )
                self.logger.info(f"{event['reporter_id']}:{event['timestamp']}")
            pipe.set("max_date_event", self.max_date_event.isoformat())
            pipe.execute()
            self.logger.info(f"Received {count} event(s) from MongoDB")
        except Exception as e:
            self.logger.error(f"Error processing events: {e}")
