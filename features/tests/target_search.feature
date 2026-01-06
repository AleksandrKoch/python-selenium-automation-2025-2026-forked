Feature: Test Scenarios for Search functionality

  Scenario: User can search for a tea
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown


  Scenario: User can search for a mug
    Given Open Target main page
    When Search for mug
    Then Search results for mug are shown


  Scenario Outline:
    Given Open Target main page
    When Search for <product>
    Then Search results for <product_result> are shown
    Examples:
      |product |product_result   |
      |coffee  |coffee           |
      |tea     |tea              |
