from dataclasses import dataclass


@dataclass
class Decision:
    """
    Represents the decision made before execution.
    """

    proceed: bool = True

    requires_confirmation: bool = False

    question: str | None = None

    modified_plan = None