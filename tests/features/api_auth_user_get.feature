@api @auth @user @get
@fixture.api
Feature: API - /auth/user GET requests

    Scenario: Retreive a list of users
        Given I am authenticated
        When I send a "get_list" request to "auth/user" endpoint
        Then I receive a list of items with the following structure "auth.user.get_list"

    Scenario: Retreive a list of users with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "auth/user" endpoint
        Then I receive an invalid token response

    Scenario: Retreive user details
        Given I am authenticated
        When I lookup the logged in user and save the "user" id
        When I send a "get" request to "auth/user" endpoint using the saved "user" id
        Then I receive the following response "auth.user.get"

    Scenario: Retreive user details with an invalid token
        Given I am authenticated
        When I lookup the logged in user and save the "user" id
        Given I am authenticated with an invalid token
        When I send a "get" request to "auth/user" endpoint using the saved "user" id
        Then I receive an invalid token response

    Scenario: Retreive user's SSH keys
        Given I am authenticated
        When I lookup the logged in user and save the "user" id
        When I send a "get_ssh_keys" request to "auth/user" endpoint using the saved "user" id
        Then I receive the following SSH keys "auth.user.get_ssh_keys"

    Scenario: Retreive user's SSH keys with an invalid token
        Given I am authenticated
        When I lookup the logged in user and save the "user" id
        Given I am authenticated with an invalid token
        When I send a "get_ssh_keys" request to "auth/user" endpoint using the saved "user" id
        Then I receive an invalid token response

    Scenario: Retreive a list of users's tokens
        Given I am authenticated
        When I lookup the logged in user and save the "user" id
        When I send a "get_tokens" request to "auth/user" endpoint using the saved "user" id
        Then I receive a list of items with the following structure "auth.user.get_tokens"

    Scenario: Retreive a list of users's tokens with an invalid token
        Given I am authenticated
        When I lookup the logged in user and save the "user" id
        Given I am authenticated with an invalid token
        When I send a "get_tokens" request to "auth/user" endpoint using the saved "user" id
        Then I receive an invalid token response
