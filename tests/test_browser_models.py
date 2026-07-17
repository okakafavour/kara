from app.browser.models import BrowserProfile, BrowserSession

print("=" * 40)
print("Testing Browser Models")
print("=" * 40)

profile = BrowserProfile(
    name="Fiverr",
    browser="chrome",
    email="okakafavour81@gmail.com",
)

session = BrowserSession(
    browser="chrome",
    profile=profile,
)

print(session)