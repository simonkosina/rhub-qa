@web @ui @e2e @qc
Feature: Basic e2e test using default configuration

Scenario: Quick Cluster full provisioning
    Given I am logged into the system with a valid user and password
    When I navigate to the quick cluster provisioning system
    When I start the quick cluster provisioning using default configuration
    Then the cluster must be provisioned and available at main page