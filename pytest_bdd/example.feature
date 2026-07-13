Feature: Herokuapp Web Testing

  Scenario: Verify the title of the login page
    Given I am on the internet home page
    When I navigate to the login page
    Then the page title should be "The Internet"

  Scenario: Verify Login with correct credentials
    Given I am on the login page
    When I enter the credentials
    Then the page header should be "Secure Area" and the success banner should be displayed
