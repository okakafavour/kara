from rich.console import Console

from app.memory.memory import Memory
from app.tools.application_tool import ApplicationTool

console = Console()


class ToolManager:
    """Routes tasks to the appropriate tool."""

    def __init__(self):
        console.log("[cyan]Tool Manager initialized[/cyan]")

        self.application = ApplicationTool()
        self.memory = Memory()

    def execute(self, task: dict):

        intent = task.get("intent", "unknown")
        entities = task.get("entities", {})

        # -------------------------
        # OPEN APPLICATION
        # -------------------------

        if intent == "open_application":

            application = entities.get("application")

            return self.application.open(application)

        # -------------------------
        # REMEMBER
        # -------------------------

        if intent == "remember":

            key = entities.get("key")
            value = entities.get("value")

            if not key or not value:
                return "I couldn't understand what to remember."

            self.memory.remember(key, value)

            return f"I'll remember that. ({key} = {value})"

        # -------------------------
        # RECALL
        # -------------------------

        if intent == "recall":

            key = entities.get("key")

            if not key:
                return "What would you like me to remember?"

            value = self.memory.recall(key)

            if value is None:
                return f"I don't know your {key} yet."

            return f"Your {key} is {value}."

        # -------------------------
        # UNKNOWN
        # -------------------------

        return "I'm not sure how to do that yet."