
Feature: Cart Functionality

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open Target home page
    When click on cart icon
    Then Your cart is empty message is shown
