from abc import ABC, abstractmethod


class BaseEventSource(ABC):
    """
    Base class for every event source.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def poll(self):
        """
        Return an Event if something happened,
        otherwise return None.
        """
        pass