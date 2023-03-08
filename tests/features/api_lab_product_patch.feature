@api @lab @product @patch
@fixture.api
Feature: API - /lab/product PATCH requests

    Scenario: Update product information
        Given I am authenticated
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        And I save the received "product" id
        When I send a "update" request to "lab/product" endpoint with body "lab.product.update" using the saved "product" id
        Then I receive the following response "lab.product.update"
    
    Scenario: Update product information with an invalid token
        Given I am authenticated
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        And I save the received "product" id
        Given I am authenticated with an invalid token
        When I send a "update" request to "lab/product" endpoint with body "lab.product.update" using the saved "product" id
        Then I receive an invalid token response
