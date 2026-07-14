from app.skills.browser.browser import BrowserEngine

print("=" * 40)
print("Testing Browser Actions")
print("=" * 40)

browser = BrowserEngine()

browser.goto("https://www.google.com")

browser.actions.wait_for("textarea")

browser.actions.type(
    "textarea",
    "Kara AI Assistant"
)

browser.actions.press(
    "textarea",
    "Enter"
)

browser.actions.wait(3000)

print("Current URL:")
print(browser.current_url())

browser.actions.screenshot("google_search.png")

print("Screenshot saved.")

input("\nPress Enter to close...")

browser.close()

print("\nBrowser Actions Test Complete")