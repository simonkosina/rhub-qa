from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.qccreation_form import QCCreation_form
from steps.get_attribute import GetAttribute
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import *
import time

@when(u'I change the reservation days date')
def step_impl(context):
    dt_request = GetAttribute()
    qc_form = QCCreation_form(context)
    
    
    reser_days = Select(qc_form.reservationdays_slct)
    reser_days.select_by_value(dt_request.get_data("reservationdz"))
    