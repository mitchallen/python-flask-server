
Feature: Hello world

  Background:
    Given the Flask app is running

  Scenario: Accessing the root URL
    When I go to the "/" URL
    Then the JSON response should contain "app" set to "src.app"

  Scenario: Accessing the hello URL
    When I go to the "/hello" URL
    Then I should be greeted with "Hello, World!"
