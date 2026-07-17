from app.profiles.manager import ProfileManager

print("=" * 40)
print("Testing Profile Manager")
print("=" * 40)

manager = ProfileManager()

print("\nBrowser Profiles\n")

for profile in manager.browser_profiles_list():
    print(profile)

print("\nWorkspaces\n")

for workspace in manager.workspaces_list():
    print(workspace)

print("\nFind Development Profile\n")

print(manager.get_browser_profile("Development"))

print("\nFind Backend Workspace\n")

print(manager.get_workspace("Backend Development"))