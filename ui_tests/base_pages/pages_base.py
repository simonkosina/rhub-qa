from multiprocessing import context
from behave import *


base_url = "http://automationpractice.com/index.php"

def login_elements(self):

    self.sing_btn = (browser.find_element_by_link_text("Sign in"))

    self.user_field = (browser.find_element_by_id("email"))

    self.password_field = (browser.find_element_by_id("passwd"))

    self.login_submmition = (browser.find_element_by_xpath("//button[@id='SubmitLogin']/span"))
  