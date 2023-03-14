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

    Scenario: Retreive group details
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an object named "rhub-admin" in the last response
        And I send a "get" request to "auth/group" endpoint using the saved "group" id
        Then I receive the following response "auth.group.get"

    Scenario: Retreive group details with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an object named "rhub-admin" in the last response
        Given I am authenticated with an invalid token
        When I send a "get" request to "auth/group" endpoint using the saved "group" id
        Then I receive an invalid token response
