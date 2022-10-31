@api @auth @user @post
@fixture.api
Feature: API - /auth/user POST requests

    Scenario: Create a new user
        Given I am authenticated
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        Then I receive the following response "auth.user.create"

    Scenario: Create a new user with an invalid token
        Given I am authenticated with an invalid token
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        Then I receive an invalid token response

    Scenario: Create a new user with a refreshed token
        Given I am authenticated with a refreshed token
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        Then I receive the following response "auth.user.create"

    Scenario: Add user to a group
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        When I send a request to add user to a group using the saved ids
        Then I receive a successful response

    Scenario: Add user to a group with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        Given I am authenticated with an invalid token
        When I send a request to add user to a group using the saved ids
        Then I receive an invalid token response

    Scenario: Add user to a group with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        Given I am authenticated with a refreshed token
        When I send a request to add user to a group using the saved ids
        Then I receive a successful response

    Scenario: Add user to a role
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        When I send a request to add user to a role using the saved ids
        Then I receive a successful response

    Scenario: Add user to a role with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        Given I am authenticated with an invalid token
        When I send a request to add user to a role using the saved ids
        Then I receive an invalid token response

    Scenario: Add user to a role with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        Given I am authenticated with a refreshed token
        When I send a request to add user to a role using the saved ids
        Then I receive a successful response
