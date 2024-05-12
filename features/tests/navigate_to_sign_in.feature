Feature: Test Scenarios for navigation to Sign In

  Scenario: Verify that a logged out user can navigate to Sign In
    Given Open Target page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened