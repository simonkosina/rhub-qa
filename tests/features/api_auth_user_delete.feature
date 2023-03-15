@api @auth @user @delete
@fixture.api
Feature: API - /auth/user DELETE requests

    Scenario: Delete an existing token
        Given I am authenticated
        When I lookup the logged in user and save the "user" id
        When I send a "create_token" request to "auth/user" endpoint with body "auth.user.create_token" using the saved "user" id
        When I save the received "token" id
        When I send a request to delete a token with id "token" from a user with id "user"
        Then I receive a successful response

    Scenario: Delete an existing token with an invalid token
        Given I am authenticated
        When I lookup the logged in user and save the "user" id
        When I send a "create_token" request to "auth/user" endpoint with body "auth.user.create_token" using the saved "user" id
        When I save the received "token" id
        Given I am authenticated with an invalid token
        When I send a request to delete a token with id "token" from a user with id "user"
        Then I receive an invalid token response
