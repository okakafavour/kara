from time import sleep

from app.events.manager import EventManager

manager = EventManager()

print("=" * 40)
print("Testing Event Polling")
print("=" * 40)

print("\nWatching for events...\n")

while True:

    events = manager.poll()

    for event in events:

        print(event)

    sleep(2)