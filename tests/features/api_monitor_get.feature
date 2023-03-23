@api @monitor @get
@fixture.api
Feature: API - /monitor/ GET requests

    Scenario: Retreive a list of BM node hosts
        Given I am authenticated
        When I send a "get_hosts" request to "monitor/bm" endpoint with body "monitor.bm.get_hosts.node"
        Then I receive a list of items with the following structure "monitor.bm.get_hosts"

    Scenario: Retreive a list of BM node hosts with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_hosts" request to "monitor/bm" endpoint with body "monitor.bm.get_hosts.app"
        Then I receive an invalid token response

    Scenario: Retreive a list of BM app hosts
        Given I am authenticated
        When I send a "get_hosts" request to "monitor/bm" endpoint with body "monitor.bm.get_hosts.app"
        Then I receive a list of items with the following structure "monitor.bm.get_hosts"

    Scenario: Retreive a list of BM app hosts with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_hosts" request to "monitor/bm" endpoint with body "monitor.bm.get_hosts.app"
        Then I receive an invalid token response

    Scenario: Get BM usage metrics
        Given I am authenticated
        When I send a "get_metrics" request to "monitor/bm" endpoint
        Then I receive a list of items with the following structure "monitor.bm.get_metrics"

    Scenario: Get BM usage metrics with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_metrics" request to "monitor/bm" endpoint
        Then I receive an invalid token response

    Scenario: Get summarized power states from BM hosts
        Given I am authenticated
        When I send a "get_power_states_metrics" request to "monitor/bm" endpoint
        Then I receive a list of items with the following structure "monitor.bm.get_power_states_metrics"

    Scenario: Get summarized power states from BM hosts with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_power_states_metrics" request to "monitor/bm" endpoint
        Then I receive an invalid token response

    Scenario: Get lab usage metrics
        Given I am authenticated
        When I send a "get_metrics" request to "monitor/lab" endpoint
        Then I receive a list of items with the following structure "monitor.lab.get_metrics"

    Scenario: Get lab usage metrics with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_metrics" request to "monitor/lab" endpoint
        Then I receive an invalid token response

    Scenario: Get VM usage metrics
        Given I am authenticated
        When I send a "get_metrics" request to "monitor/vm" endpoint
        Then I receive a list of items with the following structure "monitor.vm.get_metrics"

    Scenario: Get VM usage metrics with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_metrics" request to "monitor/vm" endpoint
        Then I receive an invalid token response
