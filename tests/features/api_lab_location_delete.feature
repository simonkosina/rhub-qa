@api @lab @location @delete
@fixture.api
Feature: API - /lab/location DELETE requests

    Scenario: Delete an existing location
        Given I am authenticated
        When I send a "create" request to "lab/location" endpoint with body "lab.location.create"
        And I save the received "location" id
        When I send a "delete" request to "lab/location" endpoint using the saved "location" id
        Then I receive a successful response

    Scenario: Delete an existing location with an invalid token
        Given I am authenticated
        When I send a "create" request to "lab/location" endpoint with body "lab.location.create"
        And I save the received "location" id
        Given I am authenticated with an invalid token
        When I send a "delete" request to "lab/location" endpoint using the saved "location" id
        Then I receive an invalid token response
