@api @lab @location @post
@fixture.api
Feature: API - /lab/location POST requests

    Scenario: Create a new location
        Given I am authenticated
        When I send a "create" request to "lab/location" endpoint with body "lab.location.create"
        Then I receive the following response "lab.location.create"

    Scenario: Create a new location with an invalid token
        Given I am authenticated with an invalid token
        When I send a "create" request to "lab/location" endpoint with body "lab.location.create"
        Then I receive an invalid token response
