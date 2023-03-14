@api @lab @region @post
@fixture.api
Feature: API - /lab/region POST requests

    Scenario: Create a new region
        Given I am authenticated
        When I send a "get_list" request to "tower/server" endpoint
        And I lookup the "tower" "id" from an object named "aap" in the last response
        And I update the "tower_id" item in "lab.region.create" using the saved "tower" id
        When I send a "get_list" request to "lab/location" endpoint
        And I lookup the "location" "id" from an object named "PNQ" in the last response
        And I update the "location_id" item in "lab.region.create" using the saved "location" id
        When I send a "get_list" request to "openstack/cloud" endpoint
        And I lookup the "openstack" "id" from an object named "osp_lab-pnq2-a" in the last response
        And I update the "openstack_id" item in "lab.region.create" using the saved "openstack" id
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an object named "rhub-admin" in the last response
        And I update the "owner_group_id" item in "lab.region.create" using the saved "group" id
        When I send a "create" request to "lab/region" endpoint with body "lab.region.create"
        Then I receive the following response "lab.region.create"

    Scenario: Create a new region
        Given I am authenticated
        When I send a "get_list" request to "tower/server" endpoint
        And I lookup the "tower" "id" from an object named "aap" in the last response
        And I update the "tower_id" item in "lab.region.create" using the saved "tower" id
        When I send a "get_list" request to "lab/location" endpoint
        And I lookup the "location" "id" from an object named "PNQ" in the last response
        And I update the "location_id" item in "lab.region.create" using the saved "location" id
        When I send a "get_list" request to "openstack/cloud" endpoint
        And I lookup the "openstack" "id" from an object named "osp_lab-pnq2-a" in the last response
        And I update the "openstack_id" item in "lab.region.create" using the saved "openstack" id
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an object named "rhub-admin" in the last response
        And I update the "owner_group_id" item in "lab.region.create" using the saved "group" id
        Given I am authenticated with an invalid token
        When I send a "create" request to "lab/region" endpoint with body "lab.region.create"
        Then I receive an invalid token response

    Scenario: Add product to a region
        Given I am authenticated
        Given I create a lab region and save the "region" id
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        And I save the received "product" id
        And I add a product with "product" id to a region with "region" id
        Then product with "product" id is enabled in a region with "region" id

    Scenario: Add product to a region with an invalid token
        Given I am authenticated
        Given I create a lab region and save the "region" id
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        And I save the received "product" id
        Given I am authenticated with an invalid token
        When I add a product with "product" id to a region with "region" id
        Then I receive an invalid token response
