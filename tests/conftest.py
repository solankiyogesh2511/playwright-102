import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def page():
    """Fixture to launch the browser and return a page object."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Set headless=True to run without UI
        context = browser.new_context(
            record_video_dir="report/videos/",
            record_video_size={"width": 640, "height": 480}
            )
        page = browser.new_page()
        yield page
        page.close()
        context.close()
        browser.close()