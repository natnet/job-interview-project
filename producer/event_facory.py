import random
import datetime
import pytz
import yaml
import logging
from Event import Event

class Event_factory:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def __init__(self, config):
        self.event_config = config
        self.counter = 0
        self.tz = pytz.timezone(self.event_config["timezone"])
       
    def create_event(self):
        try:
            metric_id = random.randint(
                self.event_config["random_range_metric_id"][0],
                self.event_config["random_range_metric_id"][1],
            )
            metric_value = random.randint(
                self.event_config["random_range_metric_value"][0],
                self.event_config["random_range_metric_value"][1],
            )
            reporter_id = self.counter + self.event_config["id_start_counting_at"]
            timestamp = datetime.datetime.now(self.tz).isoformat()
            message = self.event_config["message"]
            event = Event(reporter_id, timestamp, message, metric_value, metric_id)
            self.counter += self.event_config["id_jumps"]
            return event

        except Exception as e:
            Event_factory.logger.error(f"Failed to create event {e}")



        