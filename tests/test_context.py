from app.context.context import ContextManager

print("=" * 40)
print("Testing Context Manager")
print("=" * 40)

context = ContextManager()

# Conversation
context.add_message("Open Firefox")
context.add_message("Go to GitHub")

# Current application
context.set_application("Firefox")

# Current website
context.set_website("GitHub")

# Intent
context.set_last_intent("open_browser")

# Tool
context.set_last_tool("browser")

# Working memory
context.remember("search", "Gin Framework")

print("\nConversation")
print(context.get_conversation())

print("\nApplication")
print(context.get_application())

print("\nWebsite")
print(context.get_website())

print("\nIntent")
print(context.get_last_intent())

print("\nTool")
print(context.get_last_tool())

print("\nWorking Memory")
print(context.recall("search"))

print("\nContext Manager Test Complete")