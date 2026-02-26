import os
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright, expect

def test_hidden_subject_field():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Load the index.html file using a robust URI construction
        base_path = Path(__file__).parent.parent.resolve()
        file_path = (base_path / "index.html").as_uri()
        page.goto(file_path)

        # Verify the hidden subject field
        # <input type="hidden" name="_subject" value="New signup for NewsThread">
        hidden_input = page.locator('input[name="_subject"]')

        # Verify it exists
        expect(hidden_input).to_have_count(1)

        # Verify its attributes
        expect(hidden_input).to_have_attribute("type", "hidden")
        expect(hidden_input).to_have_attribute("value", "New signup for NewsThread")

        browser.close()
