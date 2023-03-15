@api @dns @server @patch
@fixture.api
Feature: API - /dns/server PATCH requests

    Scenario: Update DNS server information
        Given I create a DNS server and save the "server" id
        Given I am authenticated
        When I send a "update" request to "dns/server" endpoint with body "dns.server.update" using the saved "server" id
        Then I receive the following response "dns.server.update"
    
    Scenario: Update DNS server information with an invalid token
        Given I create a DNS server and save the "server" id
        Given I am authenticated with an invalid token
        When I send a "update" request to "dns/server" endpoint with body "dns.server.update" using the saved "server" id
        Then I receive an invalid token response
