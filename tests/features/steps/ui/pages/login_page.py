from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """
    Page class for the RHub login page.
    """

    locators = {
        "login_btn": (By.XPATH, "/html/body/div/div/main/div/div[1]/div[2]/button"),
        "sign_in_btn": (By.ID, "kc-login"),
        "username": (By.ID, "username"),
        "password": (By.ID, "password")
    }
