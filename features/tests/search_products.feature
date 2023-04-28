# Created by JeiM at 4/22/23
Feature: #Search products
  # Enter feature description here

  Scenario: User can search for a product that doesn't exist
    Given Open main page
    When Close pop up window
    And  Click on search icon
    And  Search for dummy product
    Then Verify No results returned on the drop-down
    When Click on predictive search
    Then Verify No results found  message is shown