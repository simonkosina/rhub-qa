# Test Automation

Test Automation
Welcome to the RHUB Automation Suite!!


	This test suite is design to cover the most usual flow occurrences in the RHUB user journey  

Definitions:
	docker - as requisit
	python 3.9 > latest-stable 
	behave latest-stable
	selenoid from https://aerokube.com/selenoid/
	requests
	

Solution design:
	The initial idea is to have a strong foundation to build the e2e tests. Based in that idea behave test framework for python was chosen. 
	The framework brings the possibility to unify API and UI tests, since every test is written in python. 
	With this in mind the actual framework enable a huge amount of possibilities when testing cross technologies, using it it's possible to create a test data mass, 
	deploy or provisioning the targeted application, run users journeys 

	

To run the tests:

Navigate to the test folder desired, all the tests are using behave so it's to easy to start then

You can choose run one by one (behave test_name.feature) or just type behave at the console into the features folder. This action will be understood by the system as that you want to run all the tests.feature in that folder.
Another option is to setup tags into the .feature files, it allows that only the .feature files that have the choosen tags will be trigged.
As an example:
 
 $bash#: behave --tags="tag"
 

 
 Running any test method with --junit option generates a .xml file reporting all selected tests results.
 
 
 behave --junit
 behave test1.feature --junit
 behave test1.feature test2.feature --junit
 behave --tags="@tag1" --junit
 
 
 The file will come with the JUnit result format.
 
 For more report formats follow https://behave.readthedocs.io/en/stable/
 
 
BRs

Allan Barroso 
abarroso@redhat.com 
+55 31 99476-9506