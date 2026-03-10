import os
from pathlib import Path
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

def test_email_input_field():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Load the index.html file
        base_path = Path(__file__).parent.parent.resolve()
        file_path = (base_path / "index.html").as_uri()
        page.goto(file_path)

        # Verify the email input field
        # <input type="email" name="email" placeholder="Enter your email" required>
        email_input = page.locator('input[name="email"]')

        # Verify it exists
        expect(email_input).to_have_count(1)

        # Verify its attributes
        expect(email_input).to_have_attribute("type", "email")
        expect(email_input).to_have_attribute("required", "")
        expect(email_input).to_have_attribute("placeholder", "Enter your email")

        browser.close()

if __name__ == "__main__":
    import sys
    try:
        print("Running test_hidden_subject_field...")
        test_hidden_subject_field()
        print("Running test_email_input_field...")
        test_email_input_field()
        print("All tests passed successfully!")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
