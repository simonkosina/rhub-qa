@web @qc @qc_sorting_by_name
Feature: My clusters page - sorting clusters by name

Scenario: QuickCluster My clusters page - sorting clusters by name

      Given I am logged into the system with a valid user and password
      When I navigate to the My Clusters menu
      When I sort the clusters in the list by name
      Then the clusters should be alphabetically arranged by their names