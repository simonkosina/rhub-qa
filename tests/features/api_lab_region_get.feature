@api @lab @region @get
@fixture.api
Feature: API - /lab/region GET requests

    Scenario: Retreive a list of regions
        Given I am authenticated
        When I send a "get_list" request to "lab/region" endpoint
        Then I receive a list of items with the following structure "lab.region.get_list"

    Scenario: Retreive a list of regions with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "lab/region" endpoint
        Then I receive an invalid token response

    Scenario: Get all region usage
        Given I am authenticated
        When I send a "get_usage_all" request to "lab/region" endpoint
        Then I receive user's usage across regions

    Scenario: Get all region usage with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_usage_all" request to "lab/region" endpoint
        Then I receive an invalid token response

    Scenario: Retreive region details
        Given I am authenticated
        Given I create a lab region and save the "region" id
        When I send a "get" request to "lab/region" endpoint using the saved "region" id
        Then I receive the following response "lab.region.get"
    
    Scenario: Retreive region details with an invalid token
        Given I create a lab region and save the "region" id
        Given I am authenticated with an invalid token
        When I send a "get" request to "lab/region" endpoint using the saved "region" id
        Then I receive an invalid token response

    Scenario: Get all products enabled in a region
        Given I am authenticated
        When I send a "get_list" request to "lab/region" endpoint
        When I lookup the "region" "id" from an object named "osp_lab-pnq2-a" in the last response
        When I send a "get_products" request to "lab/region" endpoint using the saved "region" id
        Then I receive a list of items with the following structure "lab.region.get_products"

    Scenario: Get all products enabled in a region with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "lab/region" endpoint
        When I lookup the "region" "id" from an object named "osp_lab-pnq2-a" in the last response
        Given I am authenticated with an invalid token
        When I send a "get_products" request to "lab/region" endpoint using the saved "region" id
        Then I receive an invalid token response

    Scenario: Get region usage
        Given I am authenticated
        When I send a "get_list" request to "lab/region" endpoint
        And I lookup the "region" "id" from an object named "osp_lab-pnq2-a" in the last response
        And I send a "get_usage" request to "lab/region" endpoint using the saved "region" id
        Then I receive the following response "lab.region.get_usage"

    Scenario: Get region usage with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "lab/region" endpoint
        And I lookup the "region" "id" from an object named "osp_lab-pnq2-a" in the last response
        Given I am authenticated with an invalid token
        When I send a "get_usage" request to "lab/region" endpoint using the saved "region" id
        Then I receive an invalid token response
