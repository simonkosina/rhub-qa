# FIXME: Use the new API steps
@fixture.cli
Feature: Policies

    Scenario: Get a list of existing policies
        Given   User is authenticated
        When    I execute the "policies get-list" command
        And     I get a list of policies
        Then    API and CLI outputs match

    Scenario: Create a new policy
        Given   User is authenticated
        When    I execute the "policies create --name test-policy --department test-department" command
        And     I create a policy with name "test-policy" and department "test-department"
        Then    API and CLI outputs match

    Scenario: Create a new policy with constraints
        Given   User is authenticated
        When    I execute the "policies create --name test-policy --department test-department --constraint-cost 1 --constraint-density 'very dense'" command
        And     I create a policy with name "test-policy", department "test-department" and constraints {"cost": 1, "density": "very dense"}
        Then    API and CLI outputs match
