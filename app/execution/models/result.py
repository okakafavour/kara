from dataclasses import dataclass

from app.planner.models.step import Step


@dataclass
class ExecutionResult:
    """
    Result of executing a single step.
    """

    step: Step | None
    success: bool
    message: str