@api @auth @role @patch
@fixture.api
Feature: API - auth/role PATCH requests

    Scenario: Update role information
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        When I save the received "role" id
        When I send a "update" request to "auth/role" endpoint with body "auth.role.update" using the saved "role" id
        Then I receive the following response "auth.role.update"

    Scenario: Update role information with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        When I save the received "role" id
        Given I am authenticated with an invalid token
        When I send a "update" request to "auth/role" endpoint with body "auth.role.update" using the saved "role" id
        Then I receive an invalid token response

    Scenario: Update role information with a refreshed token
        Given I am authenticated with a refreshed token
        When I send a "create" request to "auth/role" endpoint with body "auth.role.create"
        When I save the received "role" id
        When I send a "update" request to "auth/role" endpoint with body "auth.role.update" using the saved "role" id
        Then I receive the following response "auth.role.update"
