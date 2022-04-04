import time

@given(u'web address "https://rhub-app-resource-hub-dev.apps.ocp4.prod.psi.redhat.com"')
def step_impl(context):
    context.browser.get("https://rhub-app-resource-hub-dev.apps.ocp4.prod.psi.redhat.com")


@given(u'login name "testuser1" and password "testuser1"')
def step_impl(context):
    time.sleep(2)
    context.browser.maximize_window()
    context.browser.find_element_by_xpath("/html/body/div/div/main/div/div[1]/div[2]/button").click()
    context.browser.find_element_by_id("username").click()
    context.browser.find_element_by_id("username").clear()
    context.browser.find_element_by_id("username").send_keys("testuser1")
    context.browser.find_element_by_id("password").click()
    context.browser.find_element_by_id("password").clear()
    context.browser.find_element_by_id("password").send_keys("testuser1")

@when(u'i confirm pressing the sing in button')
def step_impl(context):
    context.browser.find_element_by_id("kc-login").click()


@then(u'the application should show the welcome message')
def step_impl(context):
    time.sleep(1)
    name=context.browser.find_element_by_xpath('/html/body/div/div/div/div/nav/ul/li/button').text
    assert (name == "QuickCluster")
