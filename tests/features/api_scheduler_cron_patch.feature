@api @scheduler @cron @patch
@fixture.api
Feature: API - /scheduler/cron PATCH requests

    Scenario: Update cron job information
        Given I am authenticated
        When I send a "create" request to "scheduler/cron" endpoint with body "scheduler.cron.create"
        When I save the received "cron" id
        When I send a "update" request to "scheduler/cron" endpoint with body "scheduler.cron.update" using the saved "cron" id
        Then I receive the following response "scheduler.cron.update"

    Scenario: Update cron job information with an invalid token
        Given I am authenticated
        When I send a "create" request to "scheduler/cron" endpoint with body "scheduler.cron.create"
        When I save the received "cron" id
        Given I am authenticated with an invalid token
        When I send a "update" request to "scheduler/cron" endpoint with body "scheduler.cron.update" using the saved "cron" id
        Then I receive an invalid token response

    Scenario: Update cron job information with a refreshed token
        Given I am authenticated
        When I send a "create" request to "scheduler/cron" endpoint with body "scheduler.cron.create"
        When I save the received "cron" id
        Given I am authenticated with a refreshed token
        When I send a "update" request to "scheduler/cron" endpoint with body "scheduler.cron.update" using the saved "cron" id
        Then I receive the following response "scheduler.cron.update"
