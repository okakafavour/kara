from rich.console import Console

from app.brain.rule_parser import RuleParser
from app.brain.llm_reasoner import LLMReasoner
from app.task.normalizer import TaskNormalizer

console = Console()


class Brain:
    """
    Kara's central reasoning coordinator.

    It first tries the fast rule parser.
    If no rule matches, it asks the LLM.
    Every task is normalized before being returned.
    """

    def __init__(self):
        console.log("[green]Brain initialized[/green]")

        self.rule_parser = RuleParser()
        self.reasoner = LLMReasoner()

    def process(self, command: str) -> dict:
        """
        Convert a natural language command into
        Kara's standard task format.
        """

        # Try the fast rule parser first
        task = self.rule_parser.parse(command)

        if task.get("intent") != "unknown":
            return TaskNormalizer.normalize(task)

        # Fall back to the LLM
        task = self.reasoner.reason(command)

        return TaskNormalizer.normalize(task)