
Feature: Tests for cart functionality
  # Enter feature description here

  Scenario: User can add a product to cart
     Given Open cart page
     When click cart button from side navigation
     Then Verify cart has 1 item(s)

