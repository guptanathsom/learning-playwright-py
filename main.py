from playwright.sync_api import sync_playwright


def main():
    # 1. Start Playwright and launch a visible browser
    with sync_playwright() as p:
        print("Launching browser...")
        browser = p.chromium.launch(headless=False, slow_mo=1000)

        # 2. Open a new isolated context and a fresh page tab
        context = browser.new_context()
        page = context.new_page()

        # 3. Navigate to Wikipedia
        print("Navigating to Wikipedia...")
        page.goto("https://www.wikipedia.org/")

        # 4. Locate the search input, type a query, and press Enter
        print("Searching for 'Python programming language'...")
        search_input = page.locator("input#searchInput")
        search_input.fill("Python programming language")
        search_input.press("Enter")

        # 5. Wait for the new page to load and extract the main heading
        page.wait_for_load_state("domcontentloaded")
        heading = page.locator("h1#firstHeading").inner_text()
        print(f"\nSuccessfully reached page! Heading is: '{heading}'")

        # 6. Take a screenshot of our success
        page.screenshot(path="wikipedia_python.png")
        print("Screenshot saved as 'wikipedia_python.png'")

        # 7. Clean up and close the browser
        browser.close()

if __name__ == "__main__":
    main()
