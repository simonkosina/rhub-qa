@web @qc_namepolicy @qc
Feature: Name policy

	Scenario: Name policy not satisfied
	    Given I am logged into the system with a valid user and password
     	When I navigate to the quick cluster provisioning system
		When I start the quick cluster provisioning but not satisfy the cluster name policy
     	Then I should not be able to continue to the next form page

    
    Scenario: Name policy satisfied
	    Given I am logged into the system with a valid user and password
     	When I navigate to the quick cluster provisioning system
		When I start the quick cluster provisioning and satisfy the cluster name policy
     	Then I should be able to continue to the next form page