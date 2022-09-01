@api @auth @token @post
@fixture.api
Feature: API - /auth/token POST requests

    Scenario: Create access token with valid username and password
        When I send a "create" request to "auth/token" endpoint with body "auth.token.create_valid"
        And I use the received access token
        Then I can access the API

    Scenario: Create access token with an invalid username and password
        When I send a "create" request to "auth/token" endpoint with body "auth.token.create_invalid"
        Then I receive an invalid credentials response
