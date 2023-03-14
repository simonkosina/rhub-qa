@api @lab @region @delete
@fixture.api
Feature: API - /lab/region DELETE requests

    Scenario: Delete an existing region
        Given I am authenticated
        Given I create a lab region and save the "region" id
        When I send a "delete" request to "lab/region" endpoint using the saved "region" id
        Then I receive a successful response

    Scenario: Delete an existing region using an invalid token
        Given I create a lab region and save the "region" id
        Given I am authenticated with an invalid token
        When I send a "delete" request to "lab/region" endpoint using the saved "region" id
        Then I receive an invalid token response

    Scenario: Remove product from a region
        Given I am authenticated
        Given I create a lab region and save the "region" id
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        And I save the received "product" id
        And I add a product with "product" id to a region with "region" id
        Then product with "product" id is enabled in a region with "region" id
        When I remove a product with "product" id from a region with "region" id
        Then product with "product" id is disabled in a region with "region" id

    Scenario: Remove product from a region with an invalid token
        Given I am authenticated
        Given I create a lab region and save the "region" id
        When I send a "create" request to "lab/product" endpoint with body "lab.product.create"
        And I save the received "product" id
        And I add a product with "product" id to a region with "region" id
        Then product with "product" id is enabled in a region with "region" id
        Given I am authenticated with an invalid token
        When I remove a product with "product" id from a region with "region" id
        Then I receive an invalid token response
