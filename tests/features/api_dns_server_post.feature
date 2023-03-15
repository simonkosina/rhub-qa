@api @dns @server @post
@fixture.api
Feature: API - /dns/server POST requests

    Scenario: Create a new DNS server
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an item named "rhub-admin" in the last response
        And I update the "owner_group_id" item in "dns.server.create" using the saved "group" id
        When I send a "create" request to "dns/server" endpoint with body "dns.server.create"
        Then I receive the following response "dns.server.create"

    Scenario: Create a new DNS server with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an item named "rhub-admin" in the last response
        And I update the "owner_group_id" item in "dns.server.create" using the saved "group" id
        Given I am authenticated with an invalid token
        When I send a "create" request to "dns/server" endpoint with body "dns.server.create"
        Then I receive an invalid token response
