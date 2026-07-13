from playwright.sync_api import sync_playwright

print("=" * 40)
print("Testing Browser")
print("=" * 40)

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)

    page = browser.new_page()
    page.goto("https://www.google.com")

    print("Title:", page.title())

    input("\nPress Enter to close...")

    browser.close()

print("\nBrowser Test Complete")