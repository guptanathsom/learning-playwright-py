from playwright.sync_api import sync_playwright, expect

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

        button = page.locator("button")
        button.click()

        try:
            div = page.locator("div#finish")
            expect(div.locator("h4")).to_have_text("Hello World!", timeout=5000)
            print("✅    The text 'Hello World!' was found as expected")

        except AssertionError:
            print("❌    The text 'Hello World!' was not found as expected")

        browser.close()


if __name__ == "__main__":
    main()