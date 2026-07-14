import pytest
from pytest_bdd import given, parsers, then, when,scenarios
from playwright.async_api import async_playwright,Page
import pytest_asyncio

scenarios('async_example.feature')


@pytest_asyncio.fixture
async def async_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await context.close()
        await browser.close()

@given("I am on the internet home page")
async def step_navigate_to_homepage(async_page: Page):
    await async_page.goto("https://the-internet.herokuapp.com")

@when("I navigate to the login page")
async def step_navigate_to_login_from_home(async_page: Page):
    await async_page.goto("https://the-internet.herokuapp.com/login")


@then(parsers.parse('the page title should be "{expected_title}"'))
async def step_verify_homepage_title(async_page: Page, expected_title):
    actual_title = await async_page.title()
    assert actual_title == expected_title

@given("I am on the login page")
async def step_navigate_to_login_direct(async_page: Page):
    await async_page.goto("https://the-internet.herokuapp.com/login")

@when("I enter the credentials")
async def step_enter_credentials(async_page: Page):
    search_input = async_page.locator("input#username")
    await search_input.fill("tomsmith")

    password_input = async_page.locator("input#password")
    await password_input.fill("SuperSecretPassword!")

    login_button = async_page.locator("button[type='submit']")
    await login_button.click()


@then(parsers.parse('the page header should be "{expected_title}" and the success banner should be displayed'))
async def step_verify_title_and_success_banner(async_page: Page, expected_title):
    actual_title = await async_page.locator("h2").inner_text()
    login_success_message = await async_page.locator("div.flash.success").inner_text()

    assert expected_title.strip() in actual_title.strip(), f"Expected '{expected_title}' to be in '{actual_title}'"

    assert "You logged into a secure area!" in login_success_message