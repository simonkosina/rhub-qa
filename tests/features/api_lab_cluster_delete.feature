@api @lab @cluster @delete
@fixture.api
Feature: API - /lab/cluster DELETE requests

    Scenario: Delete cluster hosts
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        When I send a "delete_hosts" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive a successful response

    Scenario: Delete cluster hosts with an invalid token
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        Given I am authenticated with an invalid token
        When I send a "delete_hosts" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive an invalid token response

    # First try with invalid to save time provisioning
    Scenario: Delete a provisoined cluster with an invalid token
        Given I am authenticated
        And a cluster with name "qageneric" is in active state
        And I save the "qageneric" cluster id as "cluster"
        And I am authenticated with an invalid token
        When I send a "delete" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive an invalid token response

    Scenario: Delete a provisioned cluster
        Given I am authenticated
        And a cluster with name "qageneric" is in active state
        And I save the "qageneric" cluster id as "cluster"
        When I send a "delete" request to "lab/cluster" endpoint using the saved "cluster" id
        Then I receive a successful response
