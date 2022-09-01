@api @auth @user @delete
@fixture.api
Feature: API - /auth/user DELETE requests

    Scenario: Delete an existing user
        Given I am authenticated
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        When I send a "delete" request to "auth/user" endpoint using the saved "user" id
        Then I receive a successful response

    Scenario: Delete an existing user with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        Given I am authenticated with an invalid token
        When I send a "delete" request to "auth/user" endpoint using the saved "user" id
        Then I receive an invalid token response

    Scenario: Delete an existing user with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        Given I am authenticated with a refreshed token
        When I send a "delete" request to "auth/user" endpoint using the saved "user" id
        Then I receive a successful response

    Scenario: Remove user from a group
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        And I send a request to add user to a group using the saved ids
        When I send a request to remove user from a group using the saved ids
        Then I receive a successful response

    Scenario: Remove user from a group with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        And I send a request to add user to a group using the saved ids
        Given I am authenticated with an invalid token
        When I send a request to remove user from a group using the saved ids
        Then I receive an invalid token response

    Scenario: Remove user from a group with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        And I send a request to add user to a group using the saved ids
        Given I am authenticated with a refreshed token
        When I send a request to remove user from a group using the saved ids
        Then I receive a successful response

    Scenario: Remove user from a role
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        And I send a request to add user to a role using the saved ids
        When I send a request to remove user from a role using the saved ids
        Then I receive a successful response

    Scenario: Remove user from a role with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        And I send a request to add user to a role using the saved ids
        Given I am authenticated with an invalid token
        When I send a request to remove user from a role using the saved ids
        Then I receive an invalid token response

    Scenario: Remove user from a role with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        And I send a request to add user to a role using the saved ids
        Given I am authenticated with a refreshed token
        When I send a request to remove user from a role using the saved ids
        Then I receive a successful response
