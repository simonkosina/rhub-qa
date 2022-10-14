from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.qccreation_form import QCCreation_form
from steps.get_attribute import GetAttribute
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from behave import *
import time


@given(u'I am logged into the system with a valid user and password')
def step_impl(context):

    dt_request = GetAttribute()
    login_page = LoginPage(context)
    login_page.visit(dt_request.get_data("url"))
    login_page = LoginPage(context)
    login_page.login_btn.click()
    login_page.input(login_page.username, dt_request.get_data("username"))
    login_page.input(login_page.password, dt_request.get_data("password"))
    login_page = LoginPage(context)
    login_page.sign_in_btn.click()
    main_page = MainPage(context)
    
    time.sleep(3)
    
    qc_menu = main_page.quickcluster_btn.text

    assert(qc_menu == "QuickCluster")


@when(u'I navigate to the quick cluster provisioning system')
def step_impl(context):
    main_page = MainPage(context)
    main_page.quickcluster_btn.click()
    time.sleep(1)
    main_page.mycluster_mn.click()
    time.sleep(3)
    main_page.newcluster_btn.click()
    time.sleep(8)

@when(u'I start the quick cluster provisioning using default configuration')
def step_impl(context):

    dt_request = GetAttribute()
    qc_form = QCCreation_form(context)

    qc_form.generic_rdbox.click()   #create class to select the right option based on the .json file

    time.sleep(3)

    qc_form.qcnext_btn.click()
    time.sleep(5) 

    qc_form.regionrdu_rdbox.click()  #create class to select the right option based on the .json file
    time.sleep(3)

    qc_form.qcnext_btn.click()
    time.sleep(5)
    
    qc_form.input(qc_form.clusterid_fld, dt_request.get_data("cluster_id"))

    qc_form.baseosimage_slct.click()
    time.sleep(3)

    qc_form.qcform_body.click()

    image = Select(qc_form.baseosimage_slct)
    image.select_by_visible_text("RHEL7.9") #get data from file
    
    time.sleep(2)

    qc_form.qcform_body.click()

    time.sleep(4)

    qc_form.qcnext_btn.click()

    time.sleep(10)

    #continue from Advanced options

@then(u'the cluster must be provisioned and available at main page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the cluster must be provisioned and available at main page')