Feature: Target cart feature

  Scenario: User can see an empty Cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

  Scenario: User can add first product from search results to cart
    Given Open Target main page
    When Search for towel
    Then Verify search results shown for towel
    When Click on Add to cart button for the first item found
    And Store product name
    And Click on Add to cart button on right side menu
    Then Validate Added to cart text is shown
    When Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product