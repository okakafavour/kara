from dataclasses import dataclass, field

from app.planner.models.step import Step


@dataclass
class ExecutionPlan:
    """
    A complete execution plan.
    """

    goal: str

    steps: list[Step] = field(default_factory=list)

    current_step: int = 0

    completed: bool = False