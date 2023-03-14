@api @lab @cluster @get
@fixture.api
Feature: API - /lab/cluster GET requests

    Scenario: Retreive a list of clusters
        Given I am authenticated
        When I send a "get_list" request to "lab/cluster" endpoint
        Then I receive a list of items with the following structure "lab.cluster.get_list"
    
    Scenario: Retreive a list of clusters with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "lab/cluster" endpoint
        Then I receive an invalid token response

    Scenario: Retreive cluster details
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        When I send a "get" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive the following response "lab.cluster.get"

    Scenario: Retreive cluster details with an invalid token
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        Given I am authenticated with an invalid token
        When I send a "get" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive an invalid token response

    Scenario: Get cluster authorized keys
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        When I send a "get_authorized_keys" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive the following SSH keys "lab.cluster.get_authorized_keys"

    Scenario: Get cluster authorized keys with an invalid token
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        Given I am authenticated with an invalid token
        When I send a "get_authorized_keys" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive the following SSH keys "lab.cluster.get_authorized_keys"

    Scenario: Get cluster event list
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        When I send a "get_events" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive a list of cluster events

    Scenario: Get cluster event list with an invalid token
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        Given I am authenticated with an invalid token
        When I send a "get_events" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive an invalid token response

    Scenario: Get cluster hosts
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        When I send a "update_hosts" request to "lab/cluster" endpoint with body "lab.cluster.update_hosts" using the saved "cluster" id
        When I send a "get_hosts" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive a list of items with the following structure "lab.cluster.get_hosts"

    Scenario: Get cluster hosts with an invalid token
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        When I send a "update_hosts" request to "lab/cluster" endpoint with body "lab.cluster.update_hosts" using the saved "cluster" id
        Given I am authenticated with an invalid token
        When I send a "get_hosts" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive an invalid token response
