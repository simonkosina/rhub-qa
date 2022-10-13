from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from behave import *

@given(u'web address "{url}"')
def step_impl(context, url):
    login_page = LoginPage(context)
    login_page.visit(url)

@given(u'login name "{name:w}" and password "{password:w}"')
def step_impl(context, name, password):
    login_page = LoginPage(context)
    login_page.login_btn.click()
    login_page.input(login_page.username, name)
    login_page.input(login_page.password, password)


@when(u'i confirm pressing the sing in button')
def step_impl(context):
    login_page = LoginPage(context)
    login_page.sign_in_btn.click()


@then(u'the application should show the welcome message')
def step_impl(context):

    main_page = MainPage(context)
    
    assert(main_page.quickcluster_btn.text == "QuickCluster")
