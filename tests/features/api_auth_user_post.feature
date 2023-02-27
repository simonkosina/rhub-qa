@api @auth @user @post
@fixture.api
Feature: API - /auth/user POST requests

    Scenario: Create a new token
        Given I am authenticated
        When I lookup the logged in user and save the "user" id
        When I send a "create_token" request to "auth/user" endpoint with body "auth.user.create_token" using the saved "user" id 
        Then I receive the following response "auth.user.create_token"

    Scenario: Create a new token with an invalid token
        Given I am authenticated
        When I lookup the logged in user and save the "user" id
        Given I am authenticated with an invalid token
        When I send a "create_token" request to "auth/user" endpoint with body "auth.user.create_token" using the saved "user" id
        Then I receive an invalid token response
