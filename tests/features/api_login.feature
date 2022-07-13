@api
Feature: Login execution for rhub api
    In order to access the system throught the api
    As a given of user I want to be able to acces the system by the api 
    So I can be connected with a valid token

Scenario:
     Given I request the token
     When  I execute the authentication
     Then  I must have access in the system
