@api @openstack @cloud @get
@fixture.api
Feature: API - /openstack GET requests

    Scenario: Retreive a list of openstack clouds
        Given I am authenticated
        When I send a "get_list" request to "openstack/cloud" endpoint
        Then I receive a list of items with the following structure "openstack.cloud.get_list"

    Scenario: Retreive a list of openstack clouds with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "openstack/cloud" endpoint
        Then I receive an invalid token response

    Scenario: Retreive openstack cloud details
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an item named "rhub-admin" in the last response
        And I update the "owner_group_id" item in "openstack.cloud.create" using the saved "group" id
        And I send a "create" request to "openstack/cloud" endpoint with body "openstack.cloud.create"
        And I save the received "cloud" id
        When I send a "get" request to "openstack/cloud" endpoint using the saved "cloud" id
        Then I receive the following response "openstack.cloud.get"

    Scenario: Retreive openstack cloud details with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an item named "rhub-admin" in the last response
        And I update the "owner_group_id" item in "openstack.cloud.create" using the saved "group" id
        And I send a "create" request to "openstack/cloud" endpoint with body "openstack.cloud.create"
        And I save the received "cloud" id
        Given I am authenticated with an invalid token
        When I send a "get" request to "openstack/cloud" endpoint using the saved "cloud" id
        Then I receive an invalid token response
