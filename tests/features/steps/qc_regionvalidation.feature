Feature: Unavailable or unselected region

	Scenario: Region validation
	    Given I am logged into the system with a valid user and password
     	When I navigate to the quick cluster provisioning system
		When I start the quick cluster provisioning using default configuration
		When I do not select a region or the region is not available
     	Then I should not be able to continue to the next form page