Feature: Tests for Target Help page UI


  Scenario: User can see main UI elements
    Given Open Target Help page
    Then Verify main header is shown
    And Verify elements shown in Search section
    Then Verify What would you like help with heading is present
    Then Verify list of 9 cards is present
    Then Verify Popular pages header is present
    Then Verify Popular pages container is present