@api @satellite @server @post
@fixture.api
Feature: API - /satellite/server POST requests

    Scenario: Create a new satellite server
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I update the "owner_group_id" item in "satellite.server.create" using the saved "group" id
        When I send a "create" request to "satellite/server" endpoint with body "satellite.server.create"
        Then I receive the following response "satellite.server.create"

    Scenario: Create a new satellite server with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I update the "owner_group_id" item in "satellite.server.create" using the saved "group" id
        Given I am authenticated with an invalid token
        When I send a "create" request to "satellite/server" endpoint with body "satellite.server.create"
        Then I receive an invalid token response
        
    Scenario: Create a new satellite server with a refreshed token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I update the "owner_group_id" item in "satellite.server.create" using the saved "group" id
        Given I am authenticated with a refreshed token
        When I send a "create" request to "satellite/server" endpoint with body "satellite.server.create"
        Then I receive the following response "satellite.server.create"
