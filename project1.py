from playwright.sync_api import sync_playwright, expect

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)

        context = browser.new_context()
        page = context.new_page()

        page.goto("https://the-internet.herokuapp.com/login")

        search_input = page.locator("input#username")
        search_input.fill("tomsmith")

        password_input = page.locator("input#password")
        password_input.fill("SuperSecretPassword!")

        login_button = page.locator("button[type='submit']")
        login_button.click()


        login_success_message = page.locator("div.flash.success")

        try:
            expect(login_success_message).to_contain_text("Kemcho Majma", timeout=2000)
            print("🚀 Success: Found the expected text!")

        except AssertionError:
            print(
                "❌ Graceful Failure: The success banner did not contain 'Kemcho Majma'."
            )

        browser.close()

# if __name__ == "__main__":
#     main()