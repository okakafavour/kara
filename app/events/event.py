from dataclasses import dataclass, field


@dataclass
class Event:
    """
    Represents an event detected on the system.
    """

    source: str
    intent: str
    entities: dict = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)