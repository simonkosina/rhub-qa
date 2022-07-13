from ui.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    """
    Page class for the RHub main page.
    """

    locators = {
        "quickcluster_btn": (By.XPATH, '/html/body/div/div/div/div/nav/ul/li/button')
    }
