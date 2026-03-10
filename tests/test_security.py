import os
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright, expect

def test_csp_frame_ancestors():
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

        # Verify frame-ancestors 'none' is present in the meta tag
        # Note: While frame-ancestors is technically ignored by browsers in meta tags,
        # it is included here as a best-practice directive for this static site.
        assert "frame-ancestors 'none';" in csp_content

        browser.close()
