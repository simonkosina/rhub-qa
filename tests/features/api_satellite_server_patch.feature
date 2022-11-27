@api @satellite @server @patch
@fixture.api
Feature: API - /satellite/server PATCH requests

    Scenario: Update satellite server information
        Given I am authenticated
        Given I create a satellite server and save the "server" id
        When I send a "update" request to "satellite/server" endpoint with body "satellite.server.update" using the saved "server" id
        Then I receive the following response "satellite.server.update"

    Scenario: Update satellite server information with an invalid token
        Given I am authenticated with an invalid token
        Given I create a satellite server and save the "server" id
        When I send a "update" request to "satellite/server" endpoint with body "satellite.server.update" using the saved "server" id
        Then I receive an invalid token response
    
    Scenario: Update satellite server information with a refreshed token
        Given I am authenticated with a refreshed token
        Given I create a satellite server and save the "server" id
        When I send a "update" request to "satellite/server" endpoint with body "satellite.server.update" using the saved "server" id
        Then I receive the following response "satellite.server.update"
