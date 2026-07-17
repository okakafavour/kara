from rich.console import Console

from app.decision.engine import DecisionEngine
from app.execution.models.result import ExecutionResult

console = Console()


class ExecutionEngine:
    """
    Executes an execution plan.

    Before executing any step, the DecisionEngine is asked to
    evaluate the plan. If a decision rule blocks execution,
    the engine returns immediately with the reason.
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

        # Think before executing
        self.decision_engine = DecisionEngine()

    def execute(self, plan):

        # ---------------------------------
        # Evaluate the plan first
        # ---------------------------------

        decision = self.decision_engine.evaluate(
            plan,
            self.session,
        )

        if not decision.proceed:

            return [
                ExecutionResult(
                    step=None,
                    success=False,
                    message=decision.question,
                )
            ]

        # ---------------------------------
        # Execute the plan
        # ---------------------------------

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

            message = skill.execute(
                {
                    "intent": step.intent,
                    "entities": step.entities,
                    "metadata": step.metadata,
                }
            )

            # ---------------------------------
            # Update session
            # ---------------------------------

            self.update_session(step)

            step.status = "completed"

            results.append(
                ExecutionResult(
                    step=step,
                    success=True,
                    message=message,
                )
            )

        return results

    def update_session(self, step):
        """
        Keep Kara's session state synchronized with what
        was actually executed.
        """

        if step.intent == "open_application":

            app = step.entities["application"]

            self.session.application_started(app)

        elif step.intent == "browser_open":

            url = step.entities["url"]

            self.session.browser_tab(
                browser="firefox",
                title=url,
                url=url,
            )

        elif step.intent == "start_workspace":

            workspace = step.entities["workspace"]

            self.session.workspace_started(workspace)