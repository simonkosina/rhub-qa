@api @login
@fixture.api
Feature: Login process for the RHub API
    The user needs to authenticate himself in order to have access to the API.

    Scenario:
        Given I request the token
        When I update the Authorization header
        Then I can access the API

    Scenario:
        Given I request the token with invalid authentication
        Then The token request fails

    Scenario:
        When I update the Authorization header with an invalid token
        Then I receive an invalid token response

    Scenario:
        Given I request the token
        When I update the Authorization header
        Then I can access the API
        When the access token expires
        Then I receive an invalid token response

    Scenario:
        Given I request the token
        When I update the Authorization header
        Then I can access the API
        When the access token expires
        And I execute token refresh
        And I update the Authorization header
        Then I can access the API
