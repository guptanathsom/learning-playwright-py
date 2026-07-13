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
