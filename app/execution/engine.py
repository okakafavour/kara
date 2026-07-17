from dataclasses import dataclass

from rich.console import Console

from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step

console = Console()


@dataclass
class ExecutionResult:
    """
    Result of executing one step.
    """

    step: Step
    success: bool
    message: str


class ExecutionEngine:
    """
    Executes an ExecutionPlan one step at a time.
    """

    def __init__(self, skill_manager, context):
        self.skill_manager = skill_manager
        self.context = context

    def execute(self, plan: ExecutionPlan) -> list[ExecutionResult]:

        results = []

        for step in plan.steps:

            console.log(f"[cyan]Executing:[/cyan] {step.intent}")

            self.context.set_last_tool(step.intent)

            try:

                response = self.skill_manager.execute(
                    {
                        "intent": step.intent,
                        "entities": step.entities,
                        "metadata": step.metadata,
                    }
                )

                step.status = "completed"

                results.append(
                    ExecutionResult(
                        step=step,
                        success=True,
                        message=response,
                    )
                )

            except Exception as error:

                step.status = "failed"

                results.append(
                    ExecutionResult(
                        step=step,
                        success=False,
                        message=str(error),
                    )
                )

                break

        if all(step.status == "completed" for step in plan.steps):
            plan.completed = True

        return results