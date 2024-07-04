Feature: Target cart feature

  Scenario: User can see an empty Cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown