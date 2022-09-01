@api @auth @role @get
@fixture.api
Feature: API - /auth/role GET requests

    Scenario: Retreive a list of roles
        Given I am authenticated
        When I send a "get_list" request to "auth/role" endpoint
        Then I receive a list of items with the following structure "auth.role.get_list"

    Scenario: Retreive a list of roles with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "auth/role" endpoint
        Then I receive an invalid token response

    Scenario: Retreive a list of roles with a refreshed token
        Given I am authenticated with a refreshed token
        When I send a "get_list" request to "auth/role" endpoint
        Then I receive a list of items with the following structure "auth.role.get_list"

    Scenario: Retreive role details
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        When I save the received "role" id
        When I send a "get" request to "auth/role" endpoint using the saved "role" id
        Then I receive the following response "auth.role.get"

    Scenario: Retreive role details with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        When I save the received "role" id
        Given I am authenticated with an invalid token
        When I send a "get" request to "auth/role" endpoint using the saved "role" id
        Then I receive an invalid token response

    Scenario: Retreive role details with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        When I save the received "role" id
        Given I am authenticated with a refreshed token
        When I send a "get" request to "auth/role" endpoint using the saved "role" id
        Then I receive the following response "auth.role.get"
