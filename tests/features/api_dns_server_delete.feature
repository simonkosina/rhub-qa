@api @dns @server @delete
@fixture.api
Feature: API - /dns/server DELETE requests

    Scenario: Delete an existing DNS server
        Given I create a DNS server and save the "server" id
        Given I am authenticated
        When I send a "delete" request to "dns/server" endpoint using the saved "server" id
        Then I receive a successful response

    Scenario: Delete an existing DNS server with an invalid token
        Given I create a DNS server and save the "server" id
        Given I am authenticated with an invalid token
        When I send a "delete" request to "dns/server" endpoint using the saved "server" id
        Then I receive an invalid token response

    Scenario: Delete an existing DNS server with a refreshed token
        Given I create a DNS server and save the "server" id
        Given I am authenticated with a refreshed token
        When I send a "delete" request to "dns/server" endpoint using the saved "server" id
        Then I receive a successful response
