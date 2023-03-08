@api @lab @product @delete
@fixture.api
Feature: API - /lab/product DELETE requests

    Scenario: Delete an existing product
        Given I am authenticated
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        And I save the received "product" id
        When I send a "delete" request to "lab/product" endpoint using the saved "product" id
        Then I receive a successful response

    Scenario: Delete an existing product with an invalid token
        Given I am authenticated
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        And I save the received "product" id
        Given I am authenticated with an invalid token
        When I send a "delete" request to "lab/product" endpoint using the saved "product" id
        Then I receive an invalid token response
