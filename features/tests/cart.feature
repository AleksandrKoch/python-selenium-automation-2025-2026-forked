# HW3.2
Feature: Test cases for cart

  Scenario: User can see Empty Cart message
    Given Open Target main page
    When Click on cart icon
    Then Empty cart message is shown


  Scenario: Product is added to the cart
    Given Open Target main page
    When Search for tea
    And Add product to the cart
    When Click on Cart icon in Sidenav
    Then Verify tea is added to the cart

