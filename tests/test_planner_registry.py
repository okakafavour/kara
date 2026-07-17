from app.planner.registry import PlannerRegistry

print("=" * 40)
print("Testing Planner Registry")
print("=" * 40)

registry = PlannerRegistry()

print()

for rule in registry.rules:

    print(rule.__class__.__name__)
    print(rule.intents)
    print()

print("Planner Registry Test Complete")