from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.planner.registry import PlannerRegistry


class GoalPlanner:

    def __init__(self):

        self.registry = PlannerRegistry()

    def expand(self, task):

        rule = self.registry.get_rule(task["intent"])

        if rule:
            return rule.expand(task)

        return ExecutionPlan(
            goal="Unknown",
            steps=[
                Step(
                    intent=task["intent"],
                    entities=task.get("entities", {}),
                )
            ],
        )