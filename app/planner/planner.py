from rich.console import Console

console = Console()


class Planner:
    """
    Converts a task into an execution plan.
    """

    def __init__(self):
        console.log("[magenta]Planner initialized[/magenta]")

    def create_plan(self, task: dict):

        if not task:
            return []

        # Version 1:
        # One task becomes one-step plan.
        return [task]