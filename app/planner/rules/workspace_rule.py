from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.planner.rules.base import BasePlanningRule
from app.profiles.manager import ProfileManager


class WorkspaceRule(BasePlanningRule):
    """
    Planning rule that expands a workspace into
    a sequence of executable steps.
    """

    def __init__(self):
        self.profiles = ProfileManager()

    @property
    def intents(self) -> list[str]:
        return [
            "start_workspace",
        ]

    def expand(self, task: dict) -> ExecutionPlan:

        workspace_name = task["entities"]["workspace"]

        workspace = self.profiles.get_workspace(
            workspace_name
        )

        if workspace is None:

            return ExecutionPlan(
                goal=workspace_name,
                steps=[],
            )

        steps = []

        # Launch applications
        for application in workspace.applications:

            steps.append(
                Step(
                    intent="open_application",
                    entities={
                        "application": application,
                    },
                )
            )

        # Open startup URLs
        for url in workspace.startup_urls:

            steps.append(
                Step(
                    intent="browser_open",
                    entities={
                        "url": url,
                    },
                )
            )

        return ExecutionPlan(
            goal=workspace.name,
            steps=steps,
        )