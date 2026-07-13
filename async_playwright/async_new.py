from playwright.async_api import async_playwright, expect
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://the-internet.herokuapp.com/login")
        search_input = page.locator("input#username")
        await search_input.fill("tomsmith")

        password_input = page.locator("input#password")
        await password_input.fill("SuperSecretPassword!")

        login_button = page.locator("button[type='submit']")
        await login_button.click()


        login_success_message = page.locator("div.flash.success")

        try:
            await expect(login_success_message).to_contain_text("You logged into a secure area!", timeout=2000)
            print("🚀 Success: Found the expected text!")

        except AssertionError:
            print(
                f"❌ Graceful Failure: The success banner did not contain 'You logged into a secure area!' had {await login_success_message.text_content()}."
            )

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
