@web 
Feature: Login page
    As a user i want to login in the web application https://rhub-app-resource-hub-dev.apps.ocp4.prod.psi.redhat.com,
    User login test1 and password test1,
    The user was previously added at the system,
    Acceptance criteria the system must show the Username Welcome to the Resource Hub.

    Scenario: Login
        Given web address "https://rhub-app-resource-hub-dev.apps.ocp4.prod.psi.redhat.com"
        Given login name "testuser1" and password "testuser1"
        When i confirm pressing the sing in button
        Then the application should show the welcome message
