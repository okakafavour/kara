from rich.console import Console

from app.llm.manager import LLMManager
from app.llm.parser import LLMParser

console = Console()


class LLMReasoner:
    """
    Uses the LLM when the rule parser
    cannot understand a command.
    """

    def __init__(self):
        console.log("[cyan]LLM Reasoner initialized[/cyan]")

        self.manager = LLMManager()

    def reason(self, command: str) -> dict:

        response = self.manager.ask(command)

        if not response.success:
            return {
                "intent": "unknown",
                "entities": {}
            }

        task = LLMParser.parse(response.content)

        if task is None:
            return {
                "intent": "unknown",
                "entities": {}
            }

        return task