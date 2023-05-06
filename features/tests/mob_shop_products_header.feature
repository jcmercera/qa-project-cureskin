# Created by JeiM at 4/20/23
Feature: Shop products header


  Scenario: User can shop by product Sunscreens
    Given Open main page
    When Close pop up window
    And Click on "Shop by product"
    And Select sunscreens
    Then Verify the fist product is Sunscreen
