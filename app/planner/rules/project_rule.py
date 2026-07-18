from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.planner.rules.base import BasePlanningRule


class ProjectRule(BasePlanningRule):
    """
    Planning rule for continuing or switching projects.
    """

    @property
    def intents(self):
        return [
            "continue_project",
        ]

    def expand(self, task):

        entities = task.get("entities", {})

        project = entities.get("project", "")

        return ExecutionPlan(
            goal=f"Continue {project}",
            steps=[
                Step(
                    intent="continue_project",
                    entities=entities,
                )
            ],
        )