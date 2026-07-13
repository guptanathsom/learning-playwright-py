from operator import and_

from pytest_bdd import given, parsers, then, when,scenarios
from playwright.sync_api import Page

scenarios('example.feature')

@given("I am on the internet home page")
def step_navigate_to_homepage(page: Page):
    page.goto("https://the-internet.herokuapp.com")

@when("I navigate to the login page")
def step_navigate_to_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")


@then(parsers.parse('the page title should be "{expected_title}"'))
def step_verify_title(page: Page, expected_title):
    actual_title = page.title()
    assert actual_title == expected_title

@given("I am on the login page")
def step_navigate_to_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

@when("I enter the credentials")
def step_enter_credentials(page: Page):
    search_input = page.locator("input#username")
    search_input.fill("tomsmith")

    password_input = page.locator("input#password")
    password_input.fill("SuperSecretPassword!")

    login_button = page.locator("button[type='submit']")
    login_button.click()


@then(parsers.parse('the page header should be "{Secure Area}" and the success banner should be displayed'))
def step_verify_title(page: Page, expected_title):
    actual_title = page.locator("h2").inner_text()
    # login_success_message = page.locator("div.flash.success")
    assert expected_title.strip() in actual_title.strip(), f"Expected '{expected_title}' to be in '{actual_title}'"
    # assert login_success_message
