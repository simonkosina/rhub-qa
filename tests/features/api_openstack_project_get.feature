@api @openstack @project @get
@fixture.api
Feature: API - /openstack/project GET requests

    Scenario: Retreive a list of openstack projects
        Given I am authenticated
        When I send a "get_list" request to "openstack/project" endpoint
        Then I receive a list of items with the following structure "openstack.project.get_list"

    Scenario: Retreive a list of openstack projects with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "openstack/project" endpoint
        Then I receive an invalid token response

    Scenario: Retreive openstack project details
        Given I am authenticated
        When I send a "get_list" request to "openstack/project" endpoint
        And I lookup the "project" "id" from an item named "ql_admin" in the last response
        When I send a "get" request to "openstack/project" endpoint using the saved "project" id
        Then I receive the following response "openstack.project.get"

    Scenario: Retreive openstack project details with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "openstack/project" endpoint
        And I lookup the "project" "id" from an item named "ql_admin" in the last response
        Given I am authenticated with an invalid token
        When I send a "get" request to "openstack/project" endpoint using the saved "project" id
        Then I receive an invalid token response

    Scenario: Get openstack project limits
        Given I am authenticated
        When I send a "get_list" request to "openstack/project" endpoint
        And I lookup the "project" "id" from an item named "ql_admin" in the last response
        When I send a "get_limits" request to "openstack/project" endpoint using the saved "project" id
        Then I receive the following response "openstack.project.get_limits"
    
    Scenario: Get openstack project limits with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "openstack/project" endpoint
        And I lookup the "project" "id" from an item named "ql_admin" in the last response
        Given I am authenticated with an invalid token
        When I send a "get_limits" request to "openstack/project" endpoint using the saved "project" id
        Then I receive an invalid token response
