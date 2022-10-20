from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    """
    Page class for the RHub main page.
    """

    locators = {
        "rhub_navbar": (By.XPATH, '/html/body/div/div/header/div[1]/a'),
        "resources_navbar": (By.XPATH, '/html/body/div/div/header/div[2]/nav/ul/li[1]/a'),
        "admin_navbar": (By.XPATH, '/html/body/div/div/header/div[2]/nav/ul/li[2]/a'),
        "guide_navbar": (By.XPATH, '/html/body/div/div/header/div[3]/button[1]'),
        "logout_btn": (By.XPATH, '/html/body/div/div/header/div[3]/button[4]'),
        "quickcluster_btn": (By.XPATH, '/html/body/div/div/div/div/nav/ul/li/button'),
        "sharedclusters_mn": (By.XPATH,'/html/body/div/div/main/section/article/div[2]/table/thead/tr/th[2]/button'),
        "mycluster_mn": (By.XPATH, '/html/body/div[1]/div/div/div/nav/ul/li/section/ul/li[2]/a'),
        "myactivity_mn": (By.XPATH, '/html/body/div/div/div/div/nav/ul/li/section/ul/li[3]/a'),
        "newcluster_btn": (By.XPATH, '/html/body/div[1]/div/main/section/article/div[1]/a/button'),
        "mctable": (By.XPATH, '/html/body/div/div/main/section/article/div[2]/table'),
        "mcnamesorting_btn": (By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/thead/tr/th[2]/button/div/span[2]'),
        "mcownersorting_btn": (By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/thead/tr/th[3]/button'),
        "mctemplatesorting_btn": (By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/thead/tr/th[4]/button'),
        "mcgroupsorting_btn": (By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/thead/tr/th[5]/button'),
        "mcregionsorting_btn": (By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/thead/tr/th[6]/button'),
        "mcstatussorting_btn": (By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/thead/tr/th[7]/button'),
        "mcreservexpsorting_btn": (By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/thead/tr/th[8]/button'),
        "mclifespanexpsorting_btn": (By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/thead/tr/th[9]/button'),
        "manamesorting_btn": (By.XPATH, '/html/body/div/div/main/section[2]/div/div[2]/article/div[2]/table/thead/tr/th[2]/button'),
        "malocationsorting_btn": (By.XPATH, '/html/body/div/div/main/section[2]/div/div[2]/article/div[2]/table/thead/tr/th[3]/button'),
        "maclusterssorting_btn": (By.XPATH, '/html/body/div/div/main/section[2]/div/div[2]/article/div[2]/table/thead/tr/th[4]/button'),
        "mastatussorting_btn": (By.XPATH, '/html/body/div/div/main/section[2]/div/div[2]/article/div[2]/table/thead/tr/th[5]/button'),
        "maownersorting_btn": (By.XPATH, '/html/body/div/div/main/section[2]/div/div[2]/article/div[2]/table/thead/tr/th[6]/button')
    }
