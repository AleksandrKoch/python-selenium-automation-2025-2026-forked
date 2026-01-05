# HW3.3
Feature: Test cases for Sign in functionality

  Scenario: Logged out user can use Sign In functionality
    Given Open Target main page
    When User clicks Account button
    And Sidenav opened
    Then User clicks Sign in button
    And Sign in form opened


