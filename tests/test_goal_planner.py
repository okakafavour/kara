from app.planner.planner import Planner

planner = Planner()

task = {
    "intent": "browser_open",
    "entities": {
        "url": "github.com"
    }
}

plan = planner.create_plan(task)

print("=" * 40)
print("Goal Planner Test")
print("=" * 40)

print("Goal:")
print(plan.goal)

print()

for i, step in enumerate(plan.steps, start=1):
    print(f"Step {i}")
    print(step)
    print()