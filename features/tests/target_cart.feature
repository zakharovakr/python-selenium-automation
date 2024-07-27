Feature: Target cart feature

  Scenario: User can see an empty Cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

    Scenario: User can add an item to the cart
    Given Open Target main page
    When Search for towel
    And Click on Add to cart button for the first item found
    Then Verify item is displayed in the cart