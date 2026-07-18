from app.projects.manager import ProjectManager
from app.projects.models import Project

print("=" * 40)
print("Project Manager Test")
print("=" * 40)

manager = ProjectManager()

# Create

if not manager.exists("MetroPass"):

    manager.create(
        Project(
            name="MetroPass",
            backend="Go",
            frontend="Flutter",
        )
    )

print("\nProjects:")

for project in manager.list():

    print("-", project.name)

print("\nFinding MetroPass:")

print(manager.get("MetroPass"))

print("\nDeleting MetroPass...")

manager.delete("MetroPass")

print("\nRemaining Projects:")

for project in manager.list():

    print("-", project.name)