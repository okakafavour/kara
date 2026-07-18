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
        # BATTERY STATUS
        # ------------------------

        battery_questions = [
            "what's my battery",
            "what is my battery",
            "battery percentage",
            "battery level",
            "battery status",
            "how much battery",
        ]

        if any(text in command for text in battery_questions):

            return {
                "intent": "battery_status",
                "entities": {},
            }

        # ------------------------
        # CPU STATUS
        # ------------------------

        cpu_questions = [
            "cpu usage",
            "cpu status",
            "processor usage",
            "how much cpu",
        ]

        if any(text in command for text in cpu_questions):

            return {
                "intent": "cpu_status",
                "entities": {},
            }

        # ------------------------
        # MEMORY STATUS
        # ------------------------

        memory_questions = [
            "memory usage",
            "ram usage",
            "memory status",
            "how much memory",
            "how much ram",
        ]

        if any(text in command for text in memory_questions):

            return {
                "intent": "memory_status",
                "entities": {},
            }

        # ------------------------
        # DISK STATUS
        # ------------------------

        disk_questions = [
            "disk usage",
            "disk space",
            "storage usage",
            "storage left",
            "free space",
        ]

        if any(text in command for text in disk_questions):

            return {
                "intent": "disk_status",
                "entities": {},
            }

        # ------------------------
        # START WORKSPACE
        # ------------------------

        workspace_commands = [
            "start work",
            "start workspace",
            "start backend development",
            "open my workspace",
            "begin work",
        ]

        if command in workspace_commands:

            return {
                "intent": "start_workspace",
                "entities": {
                    "workspace": "Backend Development",
                },
            }

        # ------------------------
        # PROJECT COMMANDS
        # ------------------------

        project_prefixes = [
            "continue ",
            "resume ",
            "work on ",
            "switch to ",
        ]

        for prefix in project_prefixes:

            if command.startswith(prefix):

                project = original[len(prefix):].strip()

                return {
                    "intent": "continue_project",
                    "entities": {
                        "project": project,
                    },
                }

        # Handle:
        # open Uber project

        if (
            command.startswith("open ")
            and command.endswith(" project")
        ):

            project = original[5:-8].strip()

            return {
                "intent": "continue_project",
                "entities": {
                    "project": project,
                },
            }

        # ------------------------
        # OPEN APPLICATION
        # ------------------------

        if command.startswith("open "):

            app = original[5:].strip()

            return {
                "intent": "open_application",
                "entities": {
                    "application": app,
                },
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
                        "value": value.strip(),
                    },
                }

        # ------------------------
        # RECALL
        # ------------------------

        if command.startswith("what is my "):

            key = original[len("what is my "):].strip()

            return {
                "intent": "recall",
                "entities": {
                    "key": key,
                },
            }

        # ------------------------
        # UNKNOWN
        # ------------------------

        return {
            "intent": "unknown",
            "entities": {},
        }