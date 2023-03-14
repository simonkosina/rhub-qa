@api @lab @product @get
@fixture.api
Feature: API - /lab/product GET requests

    Scenario: Retreive a list of products
        Given I am authenticated
        When I send a "get_list" request to "lab/product" endpoint
        Then I receive a list of items with the following structure "lab.product.get_list"

    Scenario: Retreive a list of products with an invalid token
        Given I am authenticated with an invalid token
        When I send a "get_list" request to "lab/product" endpoint
        Then I receive an invalid token response

    Scenario: Retreive product details
        Given I am authenticated
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        And I save the received "product" id
        When I send a "get" request to "lab/product" endpoint using the saved "product" id
        Then I receive the following response "lab.product.get"

    Scenario: Retreive product details with an invalid token
        Given I am authenticated
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        And I save the received "product" id
        Given I am authenticated with an invalid token
        When I send a "get" request to "lab/product" endpoint using the saved "product" id
        Then I receive an invalid token response

    Scenario: Retreive a list of regions where a product can be installed
        Given I am authenticated
        When I send a "get_list" request to "lab/product" endpoint
        And I lookup the "product" "id" from an item named "OpenShift4 UPI" in the last response
        When I send a "get_regions" request to "lab/product" endpoint using the saved "product" id
        Then I receive a list of items with the following structure "lab.product.get_regions"

    Scenario: Retreive a list of regions where a product can be installed with an invalid token
        Given I am authenticated
        When I send a "get_list" request to "lab/product" endpoint
        And I lookup the "product" "id" from an item named "OpenShift4 UPI" in the last response
        Given I am authenticated with an invalid token
        When I send a "get_regions" request to "lab/product" endpoint using the saved "product" id
        Then I receive an invalid token response
