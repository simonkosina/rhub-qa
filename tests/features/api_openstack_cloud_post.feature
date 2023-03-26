@api @openstack @cloud @post
@fixture.api
Feature: API - /openstack/cloud POST request

    Scenario: Create an openstack cloud
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an item named "rhub-admin" in the last response
        And I update the "owner_group_id" item in "openstack.cloud.create" using the saved "group" id
        When I send a "create" request to "openstack/cloud" endpoint with body "openstack.cloud.create"
        Then I receive the following response "openstack.cloud.create"

    Scenario: Create an openstack cloud with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an item named "rhub-admin" in the last response
        And I update the "owner_group_id" item in "openstack.cloud.create" using the saved "group" id
        Given I am authenticated with an invalid token
        When I send a "create" request to "openstack/cloud" endpoint with body "openstack.cloud.create"
        Then I receive an invalid token response
