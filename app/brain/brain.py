from rich.console import Console

console = Console()


class Brain:
    """Responsible for understanding user commands."""

    def __init__(self):
        console.log("[green]Brain initialized[/green]")

    def process(self, command: str) -> dict:
        command = command.strip().lower()

        if command.startswith("open "):
            target = command.replace("open ", "", 1)

            return {
                "intent": "open_application",
                "target": target,
            }

        return {
            "intent": "unknown",
            "target": command,
        }