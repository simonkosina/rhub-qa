@api @auth @token @get
@fixture.api
Feature: API - /auth/token GET requests

    Scenario: Get authorization token info
        Given I am authenticated
        When I send a "get" request to "auth/token" endpoint
        Then I receive the following response "auth.token.get"

    Scenario: Get authorization token info with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get" request to "auth/token" endpoint
        Then I receive an invalid token response

    Scenario: Get authorization token info with a refreshed token
        Given I am authenticated with a refreshed token
        When I send a "get" request to "auth/token" endpoint
        Then I receive the following response "auth.token.get"
