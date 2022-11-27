@api @dns @server @get
@fixture.api
Feature: API - /dns/server GET requests

    Scenario: Retreive a list of DNS servers
        Given I am authenticated
        When I send a "get_list" request to "dns/server" endpoint
        Then I receive a list of items with the following structure "dns.server.get_list"

    Scenario: Retreive a list of DNS servers with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "dns/server" endpoint
        Then I receive an invalid token response

    Scenario: Retreive a list of DNS servers with a refreshed token
        Given I am authenticated with a refreshed token
        When I send a "get_list" request to "dns/server" endpoint
        Then I receive a list of items with the following structure "dns.server.get_list"

    Scenario: Retreive DNS server details
        Given I am authenticated
        Given I create a DNS server and save the "server" id
        When I send a "get" request to "dns/server" endpoint using the saved "server" id
        Then I receive the following response "dns.server.get"

    Scenario: Retreive DNS server details with an invalid token
        Given I am authenticated with an invalid token
        Given I create a DNS server and save the "server" id
        When I send a "get" request to "dns/server" endpoint using the saved "server" id
        Then I receive an invalid token response

    Scenario: Retreive DNS server details with a refreshed token
        Given I am authenticated with a refreshed token
        Given I create a DNS server and save the "server" id
        When I send a "get" request to "dns/server" endpoint using the saved "server" id
        Then I receive the following response "dns.server.get"
