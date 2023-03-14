@api @lab @cluster_event @get
@fixture.api
Feature: API - /lab/cluster_event GET requests

    Scenario: Retreive cluster event details
        Given I am authenticated
        And a cluster with name "qageneric" is in active state
        And I save the "qageneric" cluster id as "cluster"
        When I send a "get_events" request to "lab/cluster" endpoint using the saved "cluster" id
        And I lookup the "event" "id" from an item in the last response
        When I send a "get" request to "lab/cluster_event" endpoint using the saved "event" id
        Then I receive a cluster event

    Scenario: Retreive cluster event details with an invalid token
        Given I am authenticated
        And a cluster with name "qageneric" is in active state
        And I save the "qageneric" cluster id as "cluster"
        When I send a "get_events" request to "lab/cluster" endpoint using the saved "cluster" id
        And I lookup the "event" "id" from an item in the last response
        Given I am authenticated with an invalid token
        When I send a "get" request to "lab/cluster_event" endpoint using the saved "event" id
        Then I receive an invalid token response

    Scenario: Get cluster event output
        Given I am authenticated
        And a cluster with name "qageneric" is in active state
        And I save the "qageneric" cluster id as "cluster"
        When I send a "get_events" request to "lab/cluster" endpoint using the saved "cluster" id
        When I find an event of type "tower_job" in the last response and save the "event" id
        And I send a "get_stdout" request to "lab/cluster_event" endpoint using the saved "event" id
        Then I receive an event output
    
    Scenario: Get cluster event output with an invalid token
        Given I am authenticated
        And a cluster with name "qageneric" is in active state
        And I save the "qageneric" cluster id as "cluster"
        When I send a "get_events" request to "lab/cluster" endpoint using the saved "cluster" id
        When I find an event of type "tower_job" in the last response and save the "event" id
        Given I am authenticated with an invalid token
        When I send a "get_stdout" request to "lab/cluster_event" endpoint using the saved "event" id
        Then I receive an invalid token response
