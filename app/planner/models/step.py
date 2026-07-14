from dataclasses import dataclass, field


@dataclass
class Step:
    """
    One executable action.
    """

    intent: str
    entities: dict = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)

    status: str = "pending"