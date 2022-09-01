@fixture.api
Feature: Login process for RHub API
    The user needs to authentication himself in order to have access to the API.

    Scenario:
        Given I request the token
        When I execute the authentication
        Then I can access the API

    Scenario:
        Given I request the token with invalid authentication
        Then The token request fails

    Scenario:
        When I execute the authentication with an invalid token
        Then I must be denied access to the API

