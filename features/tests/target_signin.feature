Feature: Target SignIn feature

  Scenario: Logged out user can navigate to Sign In
    Given Open Target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Given Store original window
    When Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window
