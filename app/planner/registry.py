from rich.console import Console

from app.plugins.loader import PluginLoader
from app.planner.rules.base import BasePlanningRule

console = Console()


class PlannerRegistry:
    """
    Automatically discovers every planning rule.
    """

    def __init__(self):

        self.rules = []

        self.load_rules()

    def load_rules(self):
        """
        Discover every installed planning rule.
        """

        self.rules = PluginLoader.load(
            "app.planner.rules",
            BasePlanningRule,
        )

        for rule in self.rules:

            console.log(
                f"[cyan]Loaded Planning Rule:[/cyan] {rule.__class__.__name__}"
            )

    def get_rule(self, intent):

        for rule in self.rules:

            if intent in rule.intents:
                return rule

        return None