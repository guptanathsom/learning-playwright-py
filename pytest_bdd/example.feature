Feature: Herokuapp Web Testing

  Scenario: Verify the title of the login page
    Given I am on the internet home page
    When I navigate to the login page
    Then the page title should be "The Internet"