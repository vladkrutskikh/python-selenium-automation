Feature: Test Scenarios for Checking cart is empty

  Scenario: Users cart is empty
    Given Open Target page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown