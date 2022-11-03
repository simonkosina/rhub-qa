@api @policies @patch
@fixture.api
Feature: API - /policies PATCH requests

    Scenario: Update policy information
        Given I am authenticated
        When I send a "create" request to "policies" endpoint with body "policies.create"
        When I save the received "policy" id
        When I send a "update" request to "policies" endpoint with body "policies.update" using the saved "policy" id
        Then I receive the following response "policies.update"

    Scenario: Update policy information with an invalid token
        Given I am authenticated
        When I send a "create" request to "policies" endpoint with body "policies.create"
        When I save the received "policy" id
        Given I am authenticated with an invalid token
        When I send a "update" request to "policies" endpoint with body "policies.update" using the saved "policy" id
        Then I receive an invalid token response

    Scenario: Update policy information with a refreshed token
        Given I am authenticated
        When I send a "create" request to "policies" endpoint with body "policies.create"
        When I save the received "policy" id
        Given I am authenticated with a refreshed token
        When I send a "update" request to "policies" endpoint with body "policies.update" using the saved "policy" id
        Then I receive the following response "policies.update"
