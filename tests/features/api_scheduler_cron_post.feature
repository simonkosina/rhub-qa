@api @scheduler @cron @post
@fixture.api
Feature: API - /scheduler/cron POST requests

    Scenario: Create a new cron job
        Given I am authenticated
        When I send a "create" request to "scheduler/cron" endpoint with body "scheduler.cron.create"
        Then I receive the following response "scheduler.cron.create"

    Scenario: Create a new cron job with an invalid token
        Given I am authenticated with an invalid token
        When I send a "create" request to "scheduler/cron" endpoint with body "scheduler.cron.create"
        Then I receive an invalid token response

    Scenario: Create a new cron job with a refreshed token
        Given I am authenticated with a refreshed token
        When I send a "create" request to "scheduler/cron" endpoint with body "scheduler.cron.create"
        Then I receive the following response "scheduler.cron.create"
