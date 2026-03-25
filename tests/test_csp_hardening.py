from pathlib import Path
from playwright.sync_api import sync_playwright

def test_csp_no_unsafe_inline():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Load the index.html file
        base_path = Path(__file__).parent.parent.resolve()
        file_path = (base_path / "index.html").as_uri()
        page.goto(file_path)

        # Get the CSP meta tag content
        csp_meta = page.locator('meta[http-equiv="Content-Security-Policy"]')
        csp_content = csp_meta.get_attribute("content")

        # Verify 'unsafe-inline' is NOT present in the CSP
        assert "'unsafe-inline'" not in csp_content
        # Verify style-src 'self' is present
        assert "style-src 'self';" in csp_content

        browser.close()
