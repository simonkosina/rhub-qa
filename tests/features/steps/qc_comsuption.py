from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.qccreation_form import QCCreation_form
from steps.get_attribute import GetAttribute
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import *
import time


@when(u'I upgrade the node flavor')
def step_impl(context):
    dt_request = GetAttribute()
    qc_form = QCCreation_form(context)
    
    nd_flavor = Select(qc_form.nodeflavor_slct)
    nd_flavor.select_by_value(dt_request.get_data("node_flavor"))


@then(u'the consumption information should update to match the values')
def step_impl(context):
    dt_request = GetAttribute()
    qc_form = QCCreation_form(context)
    
    qc_form.nodecount_slct.send_keys((Keys.CONTROL, "a"), dt_request.get_data("node_count"))
    
    nd_flavor = Select(qc_form.nodeflavor_slct)
    nd_flavor.select_by_value(dt_request.get_data("node_flavor"))

    qc_form.input(qc_form.aditionalhd_slct, dt_request.get_data("aditionalvhd"))
    qc_form.input(qc_form.aditionalhdsize_slct, dt_request.get_data("aditionalvhdsz"))
    
    reser_days = Select(qc_form.reservationdays_slct)
    reser_days.select_by_value(dt_request.get_data("reservationdz"))
    
    qc_form.qcnext_btn.click()

    time.sleep(4)

    yum_update = Select(qc_form.yumupdate_slct) 
    yum_update.select_by_visible_text(dt_request.get_data("yumupdate"))

    time.sleep(2)

    reg_method = Select(qc_form.registrationmethod_slct)
    reg_method.select_by_visible_text(dt_request.get_data("reg_method"))

    time.sleep(2)
    
    qc_form.qcnext_btn.click()

    time.sleep(5)

    assert qc_form.product_txt.text == dt_request.get_data("prod_select")
    assert qc_form.region_txt.text == dt_request.get_data("region_select")
    
    exp_days = dt_request.get_data("reservationdz")+" days"
    assert qc_form.reservexpiration_txt.text == exp_days

    assert dt_request.get_data("node_count") in qc_form.nodecount_txt.text
    assert qc_form.nodeflavor_txt.text == dt_request.get_data("node_flavor")
    assert qc_form.nbaddtvdk_txt.text == dt_request.get_data("aditionalvhd")
    assert qc_form.szaddtvdk_txt.text == dt_request.get_data("aditionalvhdsz")
    assert qc_form.execyumupdt_txt.text == dt_request.get_data("yumupdate")
    assert qc_form.regsrc_txt.text == dt_request.get_data("reg_method")


@when(u'I add a virtual disk')
def step_impl(context):
    dt_request = GetAttribute()
    qc_form = QCCreation_form(context)
    
    qc_form.input(qc_form.aditionalhd_slct, dt_request.get_data("aditionalvhd"))
    qc_form.input(qc_form.aditionalhdsize_slct, dt_request.get_data("aditionalvhdsz"))


@when(u'I upgrade the node count')
def step_impl(context):
    dt_request = GetAttribute()
    qc_form = QCCreation_form(context)
    
    qc_form.nodecount_slct.send_keys((Keys.CONTROL, "a"), dt_request.get_data("node_count"))