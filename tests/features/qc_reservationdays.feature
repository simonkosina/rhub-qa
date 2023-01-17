Feature: Reservation days selection

    Scenario: Select the cluster reservation days
        Given I am logged into the system with a valid user and password
        When I navigate to the QuickCluster provisioning system
        When I start the QuickCluster provisioning using default configuration
        When I change the reservation days date
        Then I should be able to continue the provisioning