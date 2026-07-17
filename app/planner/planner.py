from rich.console import Console

from app.planner.goal_planner import GoalPlanner
from app.planner.models.plan import ExecutionPlan

console = Console()


class Planner:
    """
    Coordinates the planning process.

    The Planner delegates planning to the GoalPlanner,
    which expands high-level tasks into executable steps.
    """

    def __init__(self):
        console.log("[green]Planner initialized[/green]")

        self.goal_planner = GoalPlanner()

    def create_plan(self, task: dict) -> ExecutionPlan:
        """
        Convert a task into an execution plan.
        """

        return self.goal_planner.expand(task)