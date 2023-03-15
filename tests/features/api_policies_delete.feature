@api @policies @delete
@fixture.api
Feature: API - /policies DELETE requests

    Scenario: Delete an existing policy
        Given I am authenticated
        When I send a "create" request to "policies" endpoint with body "policies.create"
        And I save the received "policy" id
        When I send a "delete" request to "policies" endpoint using the saved "policy" id
        Then I receive a successful response

    Scenario: Delete an existing policy with an invalid token
        Given I am authenticated
        When I send a "create" request to "policies" endpoint with body "policies.create"
        And I save the received "policy" id
        Given I am authenticated with an invalid token
        When I send a "delete" request to "policies" endpoint using the saved "policy" id
        Then I receive an invalid token response
