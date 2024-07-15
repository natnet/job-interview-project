import random
import datetime
import pytz
import yaml
import logging


class Event:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    counter = 0

    def __init__(self, event_config):
        """
        Initialize an Event instance with the given configuration.
        Sets metric_id, metric_value, timestamp, reporter_id, and message.
        """
        try:
            tz = pytz.timezone(event_config["timezone"])

            self.metric_id = random.randint(
                event_config["random_range_metric_id"][0],
                event_config["random_range_metric_id"][1],
            )
            self.metric_value = random.randint(
                event_config["random_range_metric_value"][0],
                event_config["random_range_metric_value"][1],
            )
            self.timestamp = datetime.datetime.now(tz).isoformat()
            self.reporter_id = Event.counter + event_config["id_start_counting_at"]
            self.message = event_config["message"]
            Event.counter += event_config["id_jumps"]
        except Exception as e:
            Event.logger.error(f"Failed to create event {e}")

    def to_dict(self):
        """
        Convert the Event instance to a dictionary.
        """
        return {
            "reporter_id": self.reporter_id,
            "timestamp": self.timestamp,
            "message": self.message,
            "metric_value": self.metric_value,
            "metric_id": self.metric_id
        }
