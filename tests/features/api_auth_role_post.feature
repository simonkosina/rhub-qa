@api @auth @role @post
@fixture.api
Feature: API - /auth/role POST requests

    Scenario: Create a new role
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        Then I receive the following response "auth.role.create"

    Scenario: Create a new role with an invalid token
        Given I am authenticated with an invalid token
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        Then I receive an invalid token response

    Scenario: Create a new role with a refreshed
        Given I am authenticated with a refreshed token
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        Then I receive the following response "auth.role.create"
