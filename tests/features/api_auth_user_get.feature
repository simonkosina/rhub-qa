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

    Scenario: Retreive a list of users with a refreshed token
        Given I am authenticated with a refreshed token
        When I send a "get_list" request to "auth/user" endpoint
        Then I receive a list of items with the following structure "auth.user.get_list"

    Scenario: Retreive user details
        Given I am authenticated
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        When I send a "get" request to "auth/user" endpoint using the saved "user" id
        Then I receive the following response "auth.user.get"

    Scenario: Retreive user details with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        Given I am authenticated with an invalid token
        When I send a "get" request to "auth/user" endpoint using the saved "user" id
        Then I receive an invalid token response

    Scenario: Retreive user details with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/user" endpoint with body "auth.user.create"
        And I save the received "user" id
        Given I am authenticated with a refreshed token
        When I send a "get" request to "auth/user" endpoint using the saved "user" id
        Then I receive the following response "auth.user.get"

    Scenario: Retreive a list of groups for a user
        Given I setup a user with "3" groups and save the id
        Given I am authenticated
        When I send a "get_groups" request to "auth/user" endpoint using the saved "user" id
        Then I receive a list of items with the following structure "auth.user.get_groups"

    Scenario: Retreive a list of groups for a user with an invalid token
        Given I setup a user with "3" groups and save the id
        Given I am authenticated with an invalid token
        When I send a "get_groups" request to "auth/user" endpoint using the saved "user" id
        Then I receive an invalid token response

    Scenario: Retreive a list of groups for a user with a refreshed token
        Given I setup a user with "3" groups and save the id
        Given I am authenticated with a refreshed token
        When I send a "get_groups" request to "auth/user" endpoint using the saved "user" id
        Then I receive a list of items with the following structure "auth.user.get_groups"

    Scenario: Get user roles
        Given I setup a user with "3" roles and save the id
        Given I am authenticated
        When I send a "get_roles" request to "auth/user/" endpoint using the saved "user" id
        Then I receive a list of items with the following structure "auth.user.get_roles"

    Scenario: Get user roles with an invalid token
        Given I setup a user with "3" roles and save the id
        Given I am authenticated with an invalid token
        When I send a "get_roles" request to "auth/user" endpoint using the saved "user" id
        Then I receive an invalid token response

    Scenario: Get user roles with a refreshed token
        Given I setup a user with "3" roles and save the id
        Given I am authenticated with a refreshed token
        When I send a "get_roles" request to "auth/user" endpoint using the saved "user" id
        Then I receive a list of items with the following structure "auth.user.get_roles"
