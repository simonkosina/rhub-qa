@web @qc @qc_regmethod
Feature: Advanced options registration method change

Scenario: QuickCluster Advanced options registration method change Automation
     
     Given I am logged into the system with a valid user and password
     When I navigate to the quick cluster provisioning system
     When I change advanced option registration method
     Then I should be able to continue the provisioning

