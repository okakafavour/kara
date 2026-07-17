from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    print("Launching Chromium...")
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://example.com")

    input("Is this Chromium? Press Enter...")

    browser.close()