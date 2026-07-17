from dataclasses import dataclass

from app.planner.models.plan import ExecutionPlan


@dataclass
class PendingAction:
    """
    Represents an execution that is waiting
    for user confirmation.
    """

    plan: ExecutionPlan

    question: str

    action: str

    metadata: dict | None = None