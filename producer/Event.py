import random
import datetime
import pytz

class Event:
    reporter_id_counter = 1
    israel_tz = pytz.timezone('Asia/Jerusalem')
    def __init__(self):
        self.metric_id = random.randint(1, 10)
        self.metric_value = random.randint(1, 100)
        self.timestamp = datetime.datetime.now(Event.israel_tz).isoformat()
        self.reporter_id = Event.reporter_id_counter
        self.message = f"Hello World"
        Event.reporter_id_counter += 1

    def to_dict(self):
            return {
                "reporter_id": self.reporter_id,
                "timestamp": self.timestamp,
                "message": self.message,
                "metric_value": self.metric_value,
                "metric_id": self.metric_id
            }
