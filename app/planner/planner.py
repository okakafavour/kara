from rich.console import Console

from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step

console = Console()


class Planner:
    """
    Converts a task into an execution plan.
    """

    def __init__(self):
        console.log("[green]Planner initialized[/green]")

    def create_plan(self, task: dict) -> ExecutionPlan:

        goal = task["intent"]

        step = Step(
            intent=task["intent"],
            entities=task.get("entities", {}),
            metadata=task.get("metadata", {}),
        )

        return ExecutionPlan(
            goal=goal,
            steps=[step],
        )