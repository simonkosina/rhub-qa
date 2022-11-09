@web @qc @qc_info_review
Feature: Review Cluster information

Scenario: QuickCluster Review Cluster information match Automation

      Given I am logged into the system with a valid user and password
      When I navigate to the quick cluster provisioning system
      When I validate the cluster information and it match
      Then I should be able to finish the provisioning
