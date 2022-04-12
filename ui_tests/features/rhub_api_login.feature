@api
Feature: Login execution for rhub api
    In order to access the system throught the api
    As a given of user I want to be able to acces the system by the api 
    So that reason

Scenario:
     Given I connect to the endpoint
     When  I execute the authentication
     Then  I must be logged in the system
