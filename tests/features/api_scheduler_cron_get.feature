@api @scheduler @cron @get
@fixture.api
Feature: API - /scheduler/cron GET requests

    Scenario: Retreive a list of cron jobs
        Given I am authenticated
        When I send a "get_list" request to "scheduler/cron" endpoint
        Then I receive a list of items with the following structure "scheduler.cron.get_list"

    Scenario: Retreive a list of cron jobs with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "scheduler/cron" endpoint
        Then I receive an invalid token response

    Scenario: Retreive cron job details
        Given I am authenticated
        When I send a "create" request to "scheduler/cron" endpoint with body "scheduler.cron.create"
        When I save the received "cron" id
        When I send a "get" request to "scheduler/cron" endpoint using the saved "cron" id
        Then I receive the following response "scheduler.cron.get"

    Scenario: Retreive cron job details with an invalid token
        Given I am authenticated
        When I send a "create" request to "scheduler/cron" endpoint with body "scheduler.cron.create"
        When I save the received "cron" id
        Given I am authenticated with an invalid token
        When I send a "get" request to "scheduler/cron" endpoint using the saved "cron" id
        Then I receive an invalid token response
