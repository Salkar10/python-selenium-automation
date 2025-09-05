# Created by karima at 9/7/2025
Feature: Sign in functionality
  # Enter feature description here

  Scenario: 'sign in' page is opened
    Given Open Target home page
    When click account icon in header
    When click on Sign in button
    Then Sign in  <string> message is shown