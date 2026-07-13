from app.skills.browser.browser import BrowserEngine

print("=" * 40)
print("Testing Browser Engine")
print("=" * 40)

browser = BrowserEngine()

browser.goto("google.com")

print("Title:", browser.title())
print("URL:", browser.current_url())

input("\nPress Enter to continue...")

browser.goto("github.com")

print("Title:", browser.title())
print("URL:", browser.current_url())

input("\nPress Enter to close...")

browser.close()

print("\nBrowser Engine Test Complete")