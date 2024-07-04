Feature: Target SignIn feature

  Scenario: Logged out user can navigate to Sign In
    Given Open Target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened
