@api @auth @group @get
@fixture.api
Feature: API - /auth/group GET requests

    Scenario: Retreive a list of groups
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        Then I receive a list of items with the following structure "auth.group.get_list"

    Scenario: Retreive a list of users with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "auth/group" endpoint
        Then I receive an invalid token response

    Scenario: Retreive a list of users with a refreshed token
        Given I am authenticated with a refreshed token
        When I send a "get_list" request to "auth/group" endpoint
        Then I receive a list of items with the following structure "auth.group.get_list"

    Scenario: Retreive group details
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        When I save the received "group" id
        When I send a "get" request to "auth/group" endpoint using the saved "group" id
        Then I receive the following response "auth.group.get"

    Scenario: Retreive group details with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        When I save the received "group" id
        Given I am authenticated with an invalid token
        When I send a "get" request to "auth/group" endpoint using the saved "group" id
        Then I receive an invalid token response

    Scenario: Retreive group details with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        When I save the received "group" id
        Given I am authenticated with a refreshed token
        When I send a "get" request to "auth/group" endpoint using the saved "group" id
        Then I receive the following response "auth.group.get"

    Scenario: Retreive a list of users in a group
        Given I setup a group with "3" users and save the id
        Given I am authenticated
        When I send a "get_users" request to "auth/group" endpoint using the saved "group" id
        Then I receive a list of items with the following structure "auth.group.get_users"

    Scenario: Retreive a list of users in a group with an invalid token
        Given I setup a group with "3" users and save the id
        Given I am authenticated with an invalid token
        When I send a "get_users" request to "auth/group" endpoint using the saved "group" id
        Then I receive an invalid token response

    Scenario: Retreive a list of users in a group with a refreshed token
        Given I setup a group with "3" users and save the id
        Given I am authenticated with a refreshed token
        When I send a "get_users" request to "auth/group" endpoint using the saved "group" id
        Then I receive a list of items with the following structure "auth.group.get_users"

    Scenario: Get role list for a given group
        Given I setup a group with "3" roles and save the id
        Given I am authenticated
        When I send a "get_roles" request to "auth/group" endpoint using the saved "group" id
        Then I receive a list of items with the following structure "auth.group.get_roles"

    Scenario: Get role list for a given group with an invalid token
        Given I setup a group with "3" roles and save the id
        Given I am authenticated with an invalid token
        When I send a "get_roles" request to "auth/group" endpoint using the saved "group" id
        Then I receive an invalid token response

    Scenario: Get role list for a given group with a refreshed token
        Given I setup a group with "3" roles and save the id
        Given I am authenticated with a refreshed token
        When I send a "get_roles" request to "auth/group" endpoint using the saved "group" id
        Then I receive a list of items with the following structure "auth.group.get_roles"
