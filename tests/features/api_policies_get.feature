@api @policies @get
@fixture.api
Feature: API - /policies GET requests

    Scenario: Retreive a list of policies
        Given I am authenticated
        When I send a "get_list" request to "policies" endpoint
        Then I receive a list of items with the following structure "policies.get_list"

    Scenario: Retreive a list of users with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "policies" endpoint
        Then I receive an invalid token response

    Scenario: Retreive a list of users with a refreshed token
        Given I am authenticated with a refreshed token
        When I send a "get_list" request to "policies" endpoint
        Then I receive a list of items with the following structure "policies.get_list"

    Scenario: Retreive policy details
        Given I am authenticated
        When I send a "create" request to "policies" endpoint with body "policies.create"
        When I save the received "policy" id
        When I send a "get" request to "policies" endpoint using the saved "policy" id
        Then I receive the following response "policies.get"

    Scenario: Retreive policy details with an invalid token
        Given I am authenticated
        When I send a "create" request to "policies" endpoint with body "policies.create"
        When I save the received "policy" id
        Given I am authenticated with an invalid token
        When I send a "get" request to "policies" endpoint using the saved "policy" id
        Then I receive an invalid token response

    Scenario: Retreive policy details with a refreshed token
        Given I am authenticated
        When I send a "create" request to "policies" endpoint with body "policies.create"
        When I save the received "policy" id
        Given I am authenticated with a refreshed token
        When I send a "get" request to "policies" endpoint using the saved "policy" id
        Then I receive the following response "policies.get"
