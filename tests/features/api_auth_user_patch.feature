@api @auth @user @patch
@fixture.api
Feature: API - /auth/user PATCH requests

    Scenario: Update user information
        Given I am authenticated
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        When I save the received "user" id
        When I send a "update" request to "auth/user" endpoint with body "auth.user.update" using the saved "user" id
        Then I receive the following response "auth.user.update"

    Scenario: Update user information with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        When I save the received "user" id
        Given I am authenticated with an invalid token
        When I send a "update" request to "auth/user" endpoint with body "auth.user.update" using the saved "user" id
        Then I receive an invalid token response

    Scenario: Update user information with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        When I save the received "user" id
        Given I am authenticated with a refreshed token
        When I send a "update" request to "auth/user" endpoint with body "auth.user.update" using the saved "user" id
        Then I receive the following response "auth.user.update"
