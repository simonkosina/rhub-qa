@api @scheduler @cron @delete
@fixture.api
Feature: API - /scheduler/cron DELETE requests

    Scenario: Delete an existing cron job
        Given I am authenticated
        When I send a "create" request to "scheduler/cron" endpoint with body "scheduler.cron.create"
        And I save the received "cron" id
        When I send a "delete" request to "scheduler/cron" endpoint using the saved "cron" id
        Then I receive a successful response

    Scenario: Delete an existing cron job with an invalid token
        Given I am authenticated
        When I send a "create" request to "scheduler/cron" endpoint with body "scheduler.cron.create"
        And I save the received "cron" id
        Given I am authenticated with an invalid token
        When I send a "delete" request to "scheduler/cron" endpoint using the saved "cron" id
        Then I receive an invalid token response
