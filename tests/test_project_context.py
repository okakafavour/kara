from app.projects.context import ProjectContext

print("=" * 40)
print("Project Context Test")
print("=" * 40)

context = ProjectContext()

context.set_current("Uber")

print()

print("Current Project")
print(context.current())

print()

context.clear()

print("After Clear")
print(context.current())