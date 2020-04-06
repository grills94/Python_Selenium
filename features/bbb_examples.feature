Feature: Login paths
  As a regular BBC user
  I want to be able to easily use the login features

  Scenario: I can access the sign in page from the home page
    Given I can access the home page
    When I click the sign in link
    Then the account page is available

