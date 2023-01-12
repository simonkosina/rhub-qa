Feature: Consumption update 

Scenario: node flavor upgrade
    Given I am logged into the system with a valid user and password
    When I navigate to the QuickCluster provisioning system
    When I start the QuickCluster provisioning using default configuration
    When I upgrade the node flavor 
    Then the consumption information should update to match the values



Scenario: Consumption update virtual disks addition

    Given I am logged into the system with a valid user and password
    When I navigate to the QuickCluster provisioning system
    When I start the QuickCluster provisioning using default configuration
    When I add a virtual disk 
    Then the consumption information should update to match the values


Scenario: Consumption update node count upgrade

    Given I am logged into the system with a valid user and password
    When I navigate to the QuickCluster provisioning system
    When I start the QuickCluster provisioning using default configuration
    When I upgrade the node count 
    Then the consumption information should update to match the values