@api @lab @product @post
@fixture.api
Feature: API - /lab/product POST requests

    Scenario: Create a new product
        Given I am authenticated
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        Then I receive the following response "lab.product.create"

    Scenario: Create a new product with an invalid token
        Given I am authenticated with an invalid token
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        Then I receive an invalid token response
