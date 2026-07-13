from playwright.async_api import async_playwright, expect
import asyncio

async def scan_page_by_tag(browser, url, tag):
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(url)
    print(await page.locator(tag).text_content())
    await context.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        task1 = scan_page_by_tag(browser, "https://the-internet.herokuapp.com/login", "h2")
        task2 = scan_page_by_tag(browser, "https://the-internet.herokuapp.com/dynamic_loading/1", "h3")
        tasks = [task1, task2]

        await asyncio.gather(*tasks)
        await browser.close()