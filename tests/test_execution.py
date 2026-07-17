from app.context.context import ContextManager
from app.execution.engine import ExecutionEngine
from app.planner.models.plan import ExecutionPlan
from app.planner.models.step import Step
from app.skills.manager import SkillManager

print("=" * 40)
print("Testing Execution Engine")
print("=" * 40)

plan = ExecutionPlan(
    goal="Open Firefox",
    steps=[
        Step(
            intent="open_application",
            entities={
                "application": "firefox"
            },
        )
    ],
)

engine = ExecutionEngine(
    skill_manager=SkillManager(),
    context=ContextManager(),
)

results = engine.execute(plan)

print("\nGoal:")
print(plan.goal)

print("\nCompleted:")
print(plan.completed)

print("\nResults:")

for result in results:
    print(result)

print("\nExecution Test Complete")