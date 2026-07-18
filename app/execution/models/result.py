from dataclasses import dataclass

from app.execution.models.action_result import ActionResult
from app.planner.models.step import Step


@dataclass(slots=True)
class ExecutionResult:
    """
    Result of executing a planner step.
    """

    step: Step | None

    success: bool

    message: str | ActionResult