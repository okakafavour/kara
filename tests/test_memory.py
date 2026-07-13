from app.memory.memory import Memory


memory = Memory()

print("=" * 40)
print("Testing Memory Engine")
print("=" * 40)

memory.remember("name", "Favour")
memory.remember("language", "Go")
memory.remember("editor", "VS Code")

print("Name:", memory.recall("name"))
print("Language:", memory.recall("language"))
print("Editor:", memory.recall("editor"))

print("\nStored Memories")

for row in memory.all():
    print(f"{row['key']} = {row['value']}")

print("\nMemory Engine Test Complete")