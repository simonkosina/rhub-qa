@api @me @get
@fixture.api
Feature: API - /me GET requests

    Scenario: Get info about the logged in user
        Given I am authenticated
        When I send a "get" request to "me" endpoint
        Then I receive the following response "me.get"
