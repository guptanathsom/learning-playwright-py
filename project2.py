from playwright.sync_api import sync_playwright, expect

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)

        context = browser.new_context()
        page = context.new_page()


        page.goto("https://the-internet.herokuapp.com/dropdown")
        dropdown = page.locator("select#dropdown")
        dropdown.select_option(label="Option 2")

        try:
            expect(dropdown).to_have_value("1", timeout=1000)
            print("✅ Dropdown value is as expected")

        except AssertionError:
            print("❌    Dropdown value is not as expected")

        browser.close()

if __name__ == "__main__":
    main()