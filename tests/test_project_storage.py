from app.projects.models import Project
from app.projects.storage import ProjectStorage

print("=" * 40)
print("Project Storage Test")
print("=" * 40)

storage = ProjectStorage()

projects = [
    Project(
        name="Kara",
        backend="Python",
    ),
    Project(
        name="Uber",
        backend="Go",
    ),
]

storage.save(projects)

loaded = storage.load()

print()

for project in loaded:
    print(project)