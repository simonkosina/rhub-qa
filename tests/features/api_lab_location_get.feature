@api @lab @location @get
@fixture.api
Feature: API - /lab/location GET requests

    Scenario: Retreive a list of locations
        Given I am authenticated
        When I send a "get_list" request to "lab/location" endpoint
        Then I receive a list of items with the following structure "lab.location.get_list"

    Scenario: Retreive a list of locations with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "lab/location" endpoint
        Then I receive an invalid token response

    Scenario: Retreive location details
        Given I am authenticated
        When I send a "create" request to "lab/location" endpoint with body "lab.location.create"
        And I save the received "location" id
        When I send a "get" request to "lab/location" endpoint using the saved "location" id
        Then I receive the following response "lab.location.get"

    Scenario: Retreive location details with an invalid token
        Given I am authenticated
        When I send a "create" request to "lab/location" endpoint with body "lab.location.create"
        And I save the received "location" id
        Given I am authenticated with an invalid token
        When I send a "get" request to "lab/location" endpoint using the saved "location" id
        Then I receive an invalid token response

    Scenario: Retreive a list of regions in the location
        Given I am authenticated
        When I send a "get_list" request to "lab/location" endpoint
        And I lookup the "location" "id" from an item named "PNQ" in the last response
        And I send a "get_regions" request to "lab/location" endpoint using the saved "location" id
        Then I receive a list of items with the following structure "lab.region.get_list"

    Scenario: Retreive a list of regions in the location with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "lab/location" endpoint
        And I lookup the "location" "id" from an item named "PNQ" in the last response
        Given I am authenticated with an invalid token
        When I send a "get_regions" request to "lab/location" endpoint using the saved "location" id
        Then I receive an invalid token response
