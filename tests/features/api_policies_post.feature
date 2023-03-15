@api @policies @post
@fixture.api
Feature: API - /policies POST requests

    Scenario: Create a new policy
        Given I am authenticated
        When I send a "create" request to "policies" endpoint with body "policies.create"
        Then I receive the following response "policies.create"

    Scenario: Create a new policy with an invalid token
        Given I am authenticated with an invalid token
        When I send a "create" request to "policies" endpoint with body "policies.create"
        Then I receive an invalid token response
