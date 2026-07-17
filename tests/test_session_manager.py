from app.session.manager import SessionManager

manager = SessionManager()

print("=" * 40)
print("Testing Session Manager")
print("=" * 40)

manager.application_started("firefox")

manager.browser_tab(
    "firefox",
    "GitHub",
    "https://github.com",
)

manager.browser_tab(
    "firefox",
    "ChatGPT",
    "https://chat.openai.com",
)

manager.workspace_started(
    "Backend Development"
)

print()

print("Firefox running?")
print(manager.is_running("firefox"))

print()

print("Workspace")
print(manager.current_workspace())

print()

print("Tabs")

for tab in manager.state.browsers["firefox"].tabs:
    print(tab)