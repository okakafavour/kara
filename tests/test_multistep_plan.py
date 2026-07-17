from app.planner.planner import Planner

planner = Planner()

task = {
    "intent": "compound",

    "steps": [

        {
            "intent": "open_application",
            "entities": {
                "application": "firefox"
            }
        },

        {
            "intent": "browser_open",
            "entities": {
                "url": "github.com"
            }
        }

    ]
}

plan = planner.create_plan(task)

print("=" * 40)
print("Testing Multi-Step Planner")
print("=" * 40)

print("Goal:", plan.goal)

print()

for i, step in enumerate(plan.steps, start=1):
    print(f"Step {i}")
    print(step)
    print()