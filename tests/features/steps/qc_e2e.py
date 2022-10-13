from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from behave import *

@given(u'I am logged into the system with a valid user and password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am logged into the system with a valid user and password')


@when(u'I navigate to the quick cluster provisioning system')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I navigate to the quick cluster provisioning system')


@when(u'I start the quick cluster provisioning using default configuration')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I start the quick cluster provisioning using default configuration')


@then(u'the cluster must be provisioned and available at main page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the cluster must be provisioned and available at main page')