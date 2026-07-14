import shutil
import subprocess

from app.skills.base import BaseSkill


class ApplicationSkill(BaseSkill):
    """
    Skill responsible for launching desktop applications.
    """

    APPLICATIONS = {
        "vscode": "code",
        "code": "code",
        "firefox": "firefox",
        "chrome": "google-chrome",
        "google chrome": "google-chrome",
        "chromium": "chromium",
        "terminal": "gnome-terminal",
        "files": "nautilus",
    }

    @property
    def name(self) -> str:
        return "Application"

    @property
    def description(self) -> str:
        return "Launches desktop applications."

    @property
    def intents(self) -> list[str]:
        return [
            "open_application",
        ]

    def can_handle(self, task: dict) -> bool:
        return task.get("intent") == "open_application"

    def execute(self, task: dict):

        entities = task.get("entities", {})

        target = entities.get("application", "").lower()

        executable = self.APPLICATIONS.get(target)

        if executable is None:
            return f"I don't know how to open '{target}'."

        if shutil.which(executable) is None:
            return f"{target.title()} is not installed."

        try:
            subprocess.Popen(
                [executable],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            return f"Opening {target}..."

        except Exception as error:
            return f"Failed to open {target}: {error}"