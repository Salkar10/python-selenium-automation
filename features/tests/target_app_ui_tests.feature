
Feature:  Sign In Page Window Handling


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target sign in page
    When Store original window
    And Click Target terms and Conditions link
    And Switch to newly opened window
    Then Verify Terms and Conditions page is opened
    And  Close new window
    And  Return to original window
