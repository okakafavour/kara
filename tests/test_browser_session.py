from app.browser.session import BrowserSession

session = BrowserSession(browser="chromium")

session.goto("github.com")

input("Press Enter...")

session.close()