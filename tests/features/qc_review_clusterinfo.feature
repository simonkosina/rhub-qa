@web @qc @qc_info_review
Feature: Review Cluster information

Scenario: QuickCluster Review Cluster information match Automation

      Given I am logged into the system with a valid user and password
      When I navigate to the QuickCluster provisioning system
      When I validate the cluster information and it matches
      Then I should be able to finish the provisioning
