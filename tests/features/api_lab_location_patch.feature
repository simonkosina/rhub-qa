@api @lab @location @patch
@fixture.api
Feature: API - /lab/location PATCH requests

    Scenario: Update location information
        Given I am authenticated
        When I send a "create" request to "lab/location" endpoint with body "lab.location.create"
        And I save the received "location" id
        When I send a "update" request to "lab/location" endpoint with body "lab.location.update" using the saved "location" id
        Then I receive the following response "lab.location.update"

    Scenario: Update location information with an invalid token
        Given I am authenticated
        When I send a "create" request to "lab/location" endpoint with body "lab.location.create"
        And I save the received "location" id
        Given I am authenticated with an invalid token
        When I send a "update" request to "lab/location" endpoint with body "lab.location.update" using the saved "location" id
        Then I receive an invalid token response
