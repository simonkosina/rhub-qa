@api @lab @cluster @post
@fixture.api
Feature: API - /lab/cluster POST requests

    Scenario: Create a cluster with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "lab/product" endpoint
        And I lookup the "product" "id" from an item named "Generic" in the last response
        And I update the "product_id" item in "lab.cluster.create" using the saved "product" id
        And I send a "get_list" request to "lab/region" endpoint
        And I lookup the "region" "id" from an item named "osp_lab-pnq2-a" in the last response
        And I update the "region_id" item in "lab.cluster.create" using the saved "region" id
        And I set the expiration on cluster create request to 1h from now
        Given I am authenticated with an invalid token
        When I send a "create" request to "lab/cluster" endpoint with body "lab.cluster.create"
        Then I receive an invalid token response

    Scenario: Create a cluster
        Given I am authenticated
        When I send a "get_list" request to "lab/product" endpoint
        And I lookup the "product" "id" from an item named "Generic" in the last response
        And I update the "product_id" item in "lab.cluster.create" using the saved "product" id
        And I send a "get_list" request to "lab/region" endpoint
        And I lookup the "region" "id" from an item named "osp_lab-pnq2-a" in the last response
        And I update the "region_id" item in "lab.cluster.create" using the saved "region" id
        And I set the expiration on cluster create request to 1h from now
        When I send a "create" request to "lab/cluster" endpoint with body "lab.cluster.create"
        Then I receive the following response "lab.cluster.create"

    Scenario: Add clusters hosts
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        When I send a "update_hosts" request to "lab/cluster" endpoint with body "lab.cluster.update_hosts" using the saved "cluster" id
        Then I receive a list of items with the following structure "lab.cluster.update_hosts"

    Scenario: Add clusters hosts with an invalid token
        Given I am authenticated
        And a cluster with name "qageneric" exists
        And I save the "qageneric" cluster id as "cluster"
        Given I am authenticated with an invalid token
        When I send a "update_hosts" request to "lab/cluster" endpoint with body "lab.cluster.update_hosts" using the saved "cluster" id
        Then I receive an invalid token response

    Scenario: Reboot cluster hosts
        Given I am authenticated
        And a cluster with name "qageneric" is in active state
        And I save the "qageneric" cluster id as "cluster"
        When I send a "reboot_hosts" request to "lab/cluster" endpoint with body "lab.cluster.reboot_hosts" using the saved "cluster" id
        Then I receive a list of items with the following structure "lab.cluster.reboot_hosts"

    Scenario: Reboot cluster hosts with an invalid token
        Given I am authenticated
        And a cluster with name "qageneric" is in active state
        And I save the "qageneric" cluster id as "cluster"
        Given I am authenticated with an invalid token
        When I send a "reboot_hosts" request to "lab/cluster" endpoint with body "lab.cluster.reboot_hosts" using the saved "cluster" id
        Then I receive an invalid token response
