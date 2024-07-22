Feature: Target main page search tests

    Scenario Outline: User can search for a product
      Given Open target main page
      When Search for <product>
      Then Verify search results shown for <expected_result>
      And Verify correct search results URL opens for <expected_result>
      Examples:
      |product  |expected_result    |
      |coffee   |coffee             |
#      |tea      |tea                |
#      |iphone   |iphone             |

    Scenario: Verify that user can see product names and images
      Given Open target main page
      When Search for AirPods (3rd Generation)
      Then Verify that every product has a name and an image