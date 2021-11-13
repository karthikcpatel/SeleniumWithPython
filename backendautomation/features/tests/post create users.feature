Feature: Verify POST request on Reqres
  As a QA
  I want to run automated tests for POST requests
  so that we can confirm it is working correctly

Scenario: Verify all post requests from reqres
    Given user has access to hit all post requests
    When user hits post request for create users
    Then post request should be successful