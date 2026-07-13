from rich.console import Console

from app.tools.application_tool import ApplicationTool

console = Console()


class ToolManager:

    def __init__(self):
        console.log("[cyan]Tool Manager initialized[/cyan]")

        self.application = ApplicationTool()

    def execute(self, task: dict):

        intent = task["intent"]

        if intent == "open_application":
            return self.application.open(task["target"])

        return "I don't know how to do that yet."