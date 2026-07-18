from app.projects.manager import ProjectManager

print("=" * 40)
print("Project Update Test")
print("=" * 40)

manager = ProjectManager()

# Ensure the project exists
if not manager.exists("Uber"):
    print("Uber project not found.")
    raise SystemExit

manager.set_path(
    "Uber",
    "/home/favour/projects/uber"
)

manager.set_github(
    "Uber",
    "https://github.com/favour/uber"
)

manager.set_workspace(
    "Uber",
    "Backend Development"
)

manager.set_branch(
    "Uber",
    "develop"
)

manager.set_last_task(
    "Uber",
    "Implement JWT authentication"
)

manager.set_next_task(
    "Uber",
    "Implement refresh tokens"
)

manager.add_note(
    "Uber",
    "Use Redis for session caching."
)

project = manager.get("Uber")

print(project)