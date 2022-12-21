@api @satellite @server @get
@fixture.api
Feature: API - /satellite/server GET requests

    Scenario: Retreive a list of satellite servers
        Given I am authenticated
        When I send a "get_list" request to "satellite/server" endpoint
        Then I receive a list of items with the following structure "satellite.server.get_list"

    Scenario: Retreive a list of satellite servers with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "satellite/server" endpoint
        Then I receive an invalid token response
    
    Scenario: Retreive a list of satellite servers with a refreshed token
        Given I am authenticated with a refreshed token
        When I send a "get_list" request to "satellite/server" endpoint
        Then I receive a list of items with the following structure "satellite.server.get_list"

    Scenario: Retreive satellite server details
        Given I am authenticated
        Given I create a satellite server and save the "server" id
        When I send a "get" request to "satellite/server" endpoint using the saved "server" id
        Then I receive the following response "satellite.server.get"
    
    Scenario: Retreive satellite server details with an invalid token
        Given I am authenticated with an invalid token
        Given I create a satellite server and save the "server" id
        When I send a "get" request to "satellite/server" endpoint using the saved "server" id
        Then I receive an invalid token response
    
    Scenario: Retreive satellite server details with a refreshed token
        Given I am authenticated with a refreshed token
        Given I create a satellite server and save the "server" id
        When I send a "get" request to "satellite/server" endpoint using the saved "server" id
        Then I receive the following response "satellite.server.get"
