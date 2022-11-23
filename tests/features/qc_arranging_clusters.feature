@web @qc @qc_sorting_by_name
Feature: My clusters page - sorting clusters by name

Scenario: QuickCluster My clusters page - sorting clusters by name

      Given I am logged into the system with a valid user and password
      When I navigate to the My Clusters menu
      When I sort the clusters in the list by name
      Then the clusters should be alphabetically arranged by their name


Scenario: QuickCluster My clusters page - sorting clusters by template

      Given I am logged into the system with a valid user and password
      When I navigate to the My Clusters menu
      When I sort the clusters in the list by template
      Then the clusters should be alphabetically arranged by their template


Scenario: QuickCluster My clusters page - sorting clusters by group

      Given I am logged into the system with a valid user and password
      When I navigate to the My Clusters menu
      When I sort the clusters in the list by group
      Then the clusters should be alphabetically arranged by their group


Scenario: QuickCluster My clusters page - sorting clusters by region

      Given I am logged into the system with a valid user and password
      When I navigate to the My Clusters menu
      When I sort the clusters in the list by region
      Then the clusters should be alphabetically arranged by their region


Scenario: QuickCluster My clusters page - sorting clusters by status

      Given I am logged into the system with a valid user and password
      When I navigate to the My Clusters menu
      When I sort the clusters in the list by status
      Then the clusters should be alphabetically arranged by their status