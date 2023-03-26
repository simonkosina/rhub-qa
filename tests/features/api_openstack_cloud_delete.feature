@api @openstack @cloud @delete
@fixture.api
Feature: API - /openstack/cloud DELETE feature

    Scenario: Delete an existing openstack cloud
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an item named "rhub-admin" in the last response
        And I update the "owner_group_id" item in "openstack.cloud.create" using the saved "group" id
        And I send a "create" request to "openstack/cloud" endpoint with body "openstack.cloud.create"
        And I save the received "cloud" id
        When I send a "delete" request to "openstack/cloud" endpoint using the saved "cloud" id
        Then I receive a successful response

    Scenario: Delete an existing openstack cloud with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an item named "rhub-admin" in the last response
        And I update the "owner_group_id" item in "openstack.cloud.create" using the saved "group" id
        And I send a "create" request to "openstack/cloud" endpoint with body "openstack.cloud.create"
        And I save the received "cloud" id
        Given I am authenticated with an invalid token
        When I send a "delete" request to "openstack/cloud" endpoint using the saved "cloud" id
        Then I receive an invalid token response
