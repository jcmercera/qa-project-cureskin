# Created by JeiM at 4/26/23
Feature: Cart Functionality


  Scenario: Update Cart Functionality
    Given Open main page
    When Close pop up window
    When Click on search icon
    And Search for sunscreen
    And Click on predictive search
    And Add the first product to Cart
    And Reduce the quantity of the product to zero
    Then Verify that the cart is empty