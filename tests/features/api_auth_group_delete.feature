@api @auth @group @delete
@fixture.api
Feature: API - /auth/group DELETE requests

    Scenario: Delete an existing group
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        When I send a "delete" request to "auth/group" endpoint using the saved "group" id
        Then I receive a successful response

    Scenario: Delete an existing group with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        Given I am authenticated with an invalid token
        When I send a "delete" request to "auth/group" endpoint using the saved "group" id
        Then I receive an invalid token response

    Scenario: Delete an existing group with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        Given I am authenticated with a refreshed token
        When I send a "delete" request to "auth/group" endpoint using the saved "group" id
        Then I receive a successful response

    Scenario: Remove group from a role
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        When I send a request to add group to a role using the saved ids
        When I send a request to remove group from a role using the saved ids
        Then I receive a successful response

    Scenario: Remove group from a role with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I send a request to add group to a role using the saved ids
        Given I am authenticated with an invalid token
        When I send a request to remove group from a role using the saved ids
        Then I receive a successful response

    Scenario: Remove group from a role with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I send a request to add group to a role using the saved ids
        Given I am authenticated with a refreshed token
        When I send a request to remove group from a role using the saved ids
        Then I receive a successful response
