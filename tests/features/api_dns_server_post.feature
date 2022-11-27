@api @dns @server @post
@fixture.api
Feature: API - /dns/server POST requests

    Scenario: Create a new DNS server
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I update the "owner_group_id" item in "dns.server.create" using the saved "group" id
        When I send a "create" request to "dns/server" endpoint with body "dns.server.create"
        Then I receive the following response "dns.server.create"

    Scenario: Create a new DNS server with an invalid token
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I update the "owner_group_id" item in "dns.server.create" using the saved "group" id
        Given I am authenticated with an invalid token
        When I send a "create" request to "dns/server" endpoint with body "dns.server.create"
        Then I receive an invalid token response

    Scenario: Create a new DNS server
        Given I am authenticated
        When I send a "create" request to "auth/group" endpoint with body "auth.group.create"
        And I save the received "group" id
        And I update the "owner_group_id" item in "dns.server.create" using the saved "group" id
        Given I am authenticated with a refreshed token
        When I send a "create" request to "dns/server" endpoint with body "dns.server.create"
        Then I receive the following response "dns.server.create"
