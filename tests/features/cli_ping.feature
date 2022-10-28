# FIXME: Use the new API steps
@fixture.cli
Feature: Ping

    Scenario: Ping
        Given   User is authenticated
        When    I execute the "ping get" command
        And     I execute the ping API call
        Then    API and CLI outputs match
