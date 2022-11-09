@web @qc @qc_yum_update
Feature: Advanced options yum update

Scenario: QuickCluster Advanced options yum update Automation

      Given I am logged into the system with a valid user and password
      When I navigate to the QuickCluster provisioning system
      When I set advanced option yum update
      Then I should be able to continue the provisioning
