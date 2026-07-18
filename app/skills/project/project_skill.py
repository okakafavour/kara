from app.execution.models.action_result import ActionResult
from app.projects.context import ProjectContext
from app.skills.base import BaseSkill


class ProjectSkill(BaseSkill):
    """
    Handles switching and continuing projects.
    """

    def __init__(self):

        self.context = ProjectContext()

    @property
    def name(self):

        return "Project"

    @property
    def description(self):

        return "Manages software projects."

    @property
    def intents(self):

        return [
            "continue_project",
        ]

    def can_handle(self, task):

        return task.get("intent") in self.intents

    def execute(self, task):

        entities = task.get("entities", {})

        name = entities.get("project")

        if not name:

            return ActionResult(
                action="continue_project",
                success=False,
                payload={
                    "message": "No project was specified."
                },
            )

        project = self.context.set_current(name)

        if project is None:

            return ActionResult(
                action="continue_project",
                success=False,
                payload={
                    "project": name,
                    "message": f"Project '{name}' was not found.",
                },
            )

        return ActionResult(
            action="continue_project",
            success=True,
            payload={
                "project": project.name,
                "backend": project.backend,
                "frontend": project.frontend,
                "database": project.database,
                "branch": project.branch,
                "workspace": project.workspace,
                "last_task": project.last_task,
                "next_task": project.next_task,
            },
        )