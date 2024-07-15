from abc import ABC, abstractmethod

class IEvent(ABC):
    @abstractmethod
    def __init__(self):
        self.metric_id = None
        self.metric_value = None
        self.timestamp = None
        self.reporter_id = None
        self.message = None

    @abstractmethod
    def to_dict(self):
        pass