from app.events.manager import EventManager

manager = EventManager()

print("=" * 40)
print("Testing Event Manager")
print("=" * 40)

print()

for source in manager.sources:

    print(source.name)