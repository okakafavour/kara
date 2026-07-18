import shutil
import subprocess

from app.execution.models.action_result import ActionResult
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

        # ---------------------------------
        # Unknown application
        # ---------------------------------

        if executable is None:

            return ActionResult(
                action="open_application",
                success=False,
                payload={
                    "application": target,
                },
                error="unknown_application",
            )

        # ---------------------------------
        # Application not installed
        # ---------------------------------

        if shutil.which(executable) is None:

            return ActionResult(
                action="open_application",
                success=False,
                payload={
                    "application": target,
                },
                error="not_installed",
            )

        # ---------------------------------
        # Launch application
        # ---------------------------------

        try:

            subprocess.Popen(
                [executable],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            return ActionResult(
                action="open_application",
                success=True,
                payload={
                    "application": target,
                },
            )

        except Exception as error:

            return ActionResult(
                action="open_application",
                success=False,
                payload={
                    "application": target,
                },
                error=str(error),
            )