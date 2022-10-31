@api @auth @group @patch
@fixture.api
Feature: API - /auth/group PATCH requests

    Scenario: Update group information
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        When I save the received "group" id
        When I send a "update" request to "auth/group" endpoint with body "auth.group.update" using the saved "group" id
        Then I receive the following response "auth.group.update"

    Scenario: Update group information with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        When I save the received "group" id
        Given I am authenticated with an invalid token
        When I send a "update" request to "auth/group" endpoint with body "auth.group.update" using the saved "group" id
        Then I receive an invalid token response

    Scenario: Update group information with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        When I save the received "group" id
        Given I am authenticated with a refreshed token
        When I send a "update" request to "auth/group" endpoint with body "auth.group.update" using the saved "group" id
        Then I receive the following response "auth.group.update"
