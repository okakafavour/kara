from rich.console import Console

console = Console()


class RuleParser:
    """
    Fast rule-based parser for simple commands.
    """

    def __init__(self):
        console.log("[green]Rule Parser initialized[/green]")

    def parse(self, command: str) -> dict:

        original = command.strip()
        command = original.lower()

        # ------------------------
        # OPEN APPLICATION
        # ------------------------

        if command.startswith("open "):

            app = original[5:].strip()

            return {
                "intent": "open_application",
                "entities": {
                    "application": app
                }
            }

        # ------------------------
        # REMEMBER
        # ------------------------

        if command.startswith("remember "):

            sentence = original[9:].strip()

            if " is " in sentence:

                key, value = sentence.split(" is ", 1)

                key = key.replace("my", "").strip()

                return {
                    "intent": "remember",
                    "entities": {
                        "key": key,
                        "value": value.strip()
                    }
                }

        # ------------------------
        # RECALL
        # ------------------------

        if command.startswith("what is my "):

            key = original[len("what is my "):].strip()

            return {
                "intent": "recall",
                "entities": {
                    "key": key
                }
            }

        return {
            "intent": "unknown",
            "entities": {}
        }