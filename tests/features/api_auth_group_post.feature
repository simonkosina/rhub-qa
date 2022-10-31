@api @auth @group @post
@fixture.api
Feature: API - /auth/group POST requests

    Scenario: Create a new group
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        Then I receive the following response "auth.group.create"

    Scenario: Create a new group with an invalid token
        Given I am authenticated with an invalid token
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        Then I receive an invalid token response

    Scenario: Create a new group with a refreshed token
        Given I am authenticated with a refreshed token
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        Then I receive the following response "auth.group.create"

    Scenario: Add group to a role
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        When I send a request to add group to a role using the saved ids
        Then I receive a successful response

    Scenario: Add group to a role with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        Given I am authenticated with an invalid token
        When I send a request to add group to a role using the saved ids
        Then I receive a successful response

    Scenario: Add group to a role with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        And I save the received "role" id
        And I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        Given I am authenticated with a refreshed token
        When I send a request to add group to a role using the saved ids
        Then I receive a successful response
