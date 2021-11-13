Feature: Verify GET request on Reqres
  As a QA
  I want to run automated tests for GET requests
  so that we can confirm it is working correctly

Scenario: Verify all get requests from reqres
    Given user has access to hit all get requests
    When user hits get request for list of users
    And user hits get request for single user
    Then all requests should be successful