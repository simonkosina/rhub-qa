@api @lab @cluster @patch
@fixture.api
Feature: API - /lab/cluster PATCH requests

    Scenario: Update cluster information
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        When I send a "update" request to "lab/cluster" endpoint with body "lab.cluster.update" using the saved "cluster" id
        Then I receive the following response "lab.cluster.update"

    Scenario: Update cluster information with an invalid token
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        Given I am authenticated with an invalid token
        When I send a "update" request to "lab/cluster" endpoint with body "lab.cluster.update" using the saved "cluster" id
        Then I receive an invalid token response
