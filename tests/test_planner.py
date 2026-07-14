from app.planner.planner import Planner

planner = Planner()

task = {
    "intent": "browser_open",
    "entities": {
        "url": "github.com"
    },
    "metadata": {},
}

plan = planner.create_plan(task)

print("=" * 40)
print("Testing Planner")
print("=" * 40)

print("\nGoal:")
print(plan.goal)

print("\nSteps:")

for step in plan.steps:
    print(step)

print("\nPlanner Test Complete")