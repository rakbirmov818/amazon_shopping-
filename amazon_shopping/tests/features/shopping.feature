Feature: Online Shopping on Amazon

  Scenario: Search for a product, add to basket, and update quantity
    Given the user is on the Amazon homepage
    When the user searches for a product
    And the user adds the product to the basket
    And the user updates the quantity of the product in the basket to the desired quantity
    Then the basket should reflect the updated quantity
    And the total price should be updated accordingly