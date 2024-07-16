import random
import datetime
import pytz
import yaml
from IEvent import IEvent


class Event:
    def __init__(self, reporter_id, timestamp, message, metric_value, metric_id):
        """
        Initialize an Event instance.

        Parameters:
        reporter_id (int),timestamp (str),message (str),metric_value (int),metric_id (int).
        """
        self.reporter_id = reporter_id
        self.timestamp = timestamp
        self.message = message
        self.metric_value = metric_value
        self.metric_id = metric_id

    def to_dict(self):
        """
        Convert the Event instance to a dictionary.
        """
        return {
            "reporter_id": self.reporter_id,
            "timestamp": self.timestamp,
            "message": self.message,
            "metric_value": self.metric_value,
            "metric_id": self.metric_id,
        }
