from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("Chromium executable:")
    print(p.chromium.executable_path)

    print("\nFirefox executable:")
    print(p.firefox.executable_path)

    print("\nWebKit executable:")
    print(p.webkit.executable_path)