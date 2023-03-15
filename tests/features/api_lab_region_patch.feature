@api @lab @region @patch
@fixture.api
Feature: API - /lab/region PATCH requests

    Scenario: Update region information
        Given I am authenticated
        Given I create a lab region and save the "region" id
        When I send a "update" request to "lab/region" endpoint with body "lab.region.update" using the saved "region" id
        Then I receive the following response "lab.region.update"

    Scenario: Update region information with an invalid token
        Given I create a lab region and save the "region" id
        Given I am authenticated with an invalid token
        When I send a "update" request to "lab/region" endpoint with body "lab.region.update" using the saved "region" id
        Then I receive an invalid token response
        