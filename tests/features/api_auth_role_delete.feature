@api @auth @role @delete
@fixture.api
Feature: API - /auth/role DELETE requests

    Scenario: Delete an existing role
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        When I send a "delete" request to "auth/role" endpoint using the saved "role" id
        Then I receive a successful response

    Scenario: Delete an existing role with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        Given I am authenticated with an invalid token
        When I send a "delete" request to "auth/role" endpoint using the saved "role" id
        Then I receive an invalid token response

    Scenario: Delete an existing role with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        Given I am authenticated with a refreshed token
        When I send a "delete" request to "auth/role" endpoint using the saved "role" id
        Then I receive a successful response
