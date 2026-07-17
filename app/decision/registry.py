import importlib
import inspect
import pkgutil

from rich.console import Console

from app.decision.rules.base import BaseDecisionRule

console = Console()


class DecisionRegistry:
    """
    Automatically discovers every decision rule.
    """

    def __init__(self):

        self.rules = []

        self.load_rules()

    def load_rules(self):

        package = importlib.import_module(
            "app.decision.rules"
        )

        for _, module_name, _ in pkgutil.iter_modules(
            package.__path__
        ):

            if module_name.startswith("__"):
                continue

            if module_name == "base":
                continue

            module = importlib.import_module(
                f"app.decision.rules.{module_name}"
            )

            for _, obj in inspect.getmembers(
                module,
                inspect.isclass,
            ):

                if (
                    issubclass(obj, BaseDecisionRule)
                    and obj is not BaseDecisionRule
                ):

                    console.log(
                        f"[cyan]Loaded Decision Rule:[/cyan] {obj.__name__}"
                    )

                    self.rules.append(obj())

    def applicable_rules(
        self,
        plan,
        session,
    ):

        return [

            rule

            for rule in self.rules

            if rule.applies(
                plan,
                session,
            )

        ]