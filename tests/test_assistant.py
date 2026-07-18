from app.assistant.assistant import KaraAssistant

print("=" * 40)
print("Kara Assistant Test")
print("=" * 40)

kara = KaraAssistant()

while True:

    command = input("\nYou: ")

    if command.lower() in {"exit", "quit"}:
        break

    response = kara.process(command)

    print()
    print("Kara:")
    print(response)