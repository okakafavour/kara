from app.planner.rules.workspace_rule import WorkspaceRule

rule = WorkspaceRule()

task = {
    "intent": "start_workspace",
    "entities": {
        "workspace": "Backend Development",
    },
}

plan = rule.expand(task)

print("=" * 40)
print("Workspace Rule Test")
print("=" * 40)

print("Goal:")
print(plan.goal)

print()

for i, step in enumerate(plan.steps, start=1):

    print(f"Step {i}")
    print(step)
    print()