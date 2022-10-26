@web @region
Feature: Region validation

	Scenario: Region validation unavailable or unselected region
	    Given I am logged into the system with a valid user and password
     	When I navigate to the quick cluster provisioning system
		When I start the provisioning but I do not select a region or the region is not available
     	Then I should not be able to continue to the next form page

	
	Scenario: Region validation region right selection
	    Given I am logged into the system with a valid user and password
     	When I navigate to the quick cluster provisioning system
		When I start the provisioning and I do select a region
     	Then I should be able to continue to the next form page