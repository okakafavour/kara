from app.context.context import ContextManager
from app.execution.engine import ExecutionEngine
from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.session.manager import SessionManager
from app.skills.manager import SkillManager

plan = ExecutionPlan(
    goal="Open Firefox and GitHub",
    steps=[
        Step(
            intent="open_application",
            entities={
                "application": "firefox"
            }
        ),
        Step(
            intent="browser_open",
            entities={
                "url": "github.com"
            }
        )
    ]
)

engine = ExecutionEngine(
    skill_manager=SkillManager(),
    context=ContextManager(),
    session=SessionManager(),
)

results = engine.execute(plan)

print("=" * 40)
print("Execution Results")
print("=" * 40)

for result in results:
    print(result)