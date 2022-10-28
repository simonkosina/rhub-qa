# FIXME: Use the new API steps
@fixture.cli
Feature: Cowsay

    Scenario: Cowsay
        Given   User is authenticated
        When    I execute the "cowsay get" command
        And     I execute the cowsay API call
        Then    API and CLI outputs match
