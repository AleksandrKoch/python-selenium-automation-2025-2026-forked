# HW3.3
Feature: Test cases for Sign in functionality

  Scenario: Logged out user can open Sign In page
    Given Open Target main page
    When User clicks Account button
    And Account menu is opened
    Then User clicks Sign in button
    And Sign in page opened


