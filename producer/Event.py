import random
import datetime
import pytz
import yaml
import logging


class Event:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    counter = 0

    def __init__(self, tz, reporter_id_start_at, message, id_jumps):
        try:
            self.metric_id = random.randint(1, 10)
            self.metric_value = random.randint(1, 100)
            self.timestamp = datetime.datetime.now(tz).isoformat()
            self.reporter_id = Event.counter + reporter_id_start_at
            self.message = message
            Event.counter += id_jumps
        except Exception as e:
            Event.logger.error(f"Failed to create event {e}")

    def to_dict(self):
        return {
            "reporter_id": self.reporter_id,
            "timestamp": self.timestamp,
            "message": self.message,
            "metric_value": self.metric_value,
            "metric_id": self.metric_id,
        }
