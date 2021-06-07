Feature: Verify GET request on Reqres
  As a QA
  I want to run automated tests for GET requests
  so that we can confirm it is working correctly

Scenario: Verify get request for single and list users
    Given user hits get request for list users
    When user hits get request for single user
    Then response should be generated for both get request