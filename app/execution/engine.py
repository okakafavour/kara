from rich.console import Console

from app.execution.models.result import ExecutionResult

console = Console()


class ExecutionEngine:
    """
    Executes an already-approved execution plan.

    The DecisionEngine is responsible for deciding whether a
    plan should execute. This class only performs the execution.
    """

    def __init__(
        self,
        skill_manager,
        context,
        session,
    ):
        self.skill_manager = skill_manager
        self.context = context
        self.session = session

    def execute(self, plan):
        """
        Execute every step in the execution plan.
        """

        results = []

        for step in plan.steps:

            console.log(f"[cyan]Executing:[/cyan] {step.intent}")

            skill = self.skill_manager.find_skill(step.intent)

            if skill is None:

                results.append(
                    ExecutionResult(
                        step=step,
                        success=False,
                        message=f"No skill found for '{step.intent}'",
                    )
                )

                continue

            try:

                message = skill.execute(
                    {
                        "intent": step.intent,
                        "entities": step.entities,
                        "metadata": step.metadata,
                    }
                )

                # --------------------
                # Update Session
                # --------------------

                self.update_session(step)

                step.status = "completed"

                results.append(
                    ExecutionResult(
                        step=step,
                        success=True,
                        message=message,
                    )
                )

            except Exception as e:

                step.status = "failed"

                results.append(
                    ExecutionResult(
                        step=step,
                        success=False,
                        message=str(e),
                    )
                )

        # Mark plan complete if every step succeeded
        if all(result.success for result in results):
            plan.completed = True

        return results

    def update_session(self, step):
        """
        Keep Kara's session synchronized with
        successfully executed steps.
        """

        if step.intent == "open_application":

            self.session.application_started(
                step.entities["application"]
            )

        elif step.intent == "browser_open":

            url = step.entities["url"]

            self.session.browser_tab(
                browser="firefox",
                title=url,
                url=url,
            )

        elif step.intent == "start_workspace":

            self.session.workspace_started(
                step.entities["workspace"]
            )