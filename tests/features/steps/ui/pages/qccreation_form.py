from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class QCCreation_form(BasePage): 
    
    
    locators = {

        """
        Footer buttons locators
        """
        "next_btn": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/footer/button[1]'),
        "back_btn": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/footer/button[2]'),
        "cancel_btn": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/footer/button[3]'),
        
        """
        Product selection locators
        """
        "ceph_rdbox": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/article[1]/div[3]/div/input'),
        "fusekaraf_rdbox": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/article[2]/div[3]/div/input'),
        "generic_rdbox": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/article[3]/div[3]/div/input'),
        "gluster_rdbox": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/article[4]/div[3]/div/input'),
        "jbosseap_rdbox": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/article[5]/div[3]/div/input'),
        "openshift_rdbox": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/article[6]/div[3]/div/input'),
        "openshift4_rdbox": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/article[7]/div[3]/div/input'),
        "packstack_rdbox": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/article[8]/div[3]/div/input'),

        """
        Region selection locators
        """

        "regionrdu_rdbox": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/article/div[2]/div/div/input'),

        """
        Cluster configuration locators
        """

        "clusterid_fld": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/form/div[1]/div[2]/input'),
        "baseosimage_slct": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/form/div[2]/div[2]/select'),
        "nodecount_slct": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/form/div[3]/div[2]/input'),
        "nodeflavor_slct": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/form/div[4]/div[2]/select'),
        "aditionalhd_slct": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/form/div[5]/div[2]/input'),
        "aditionalhdsize_slct": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/form/div[6]/div[2]/input'),
        "reservationdays_slct": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/div[2]/form/div[7]/div[2]/select'),

        """"
        Advanced options
        """
        "yumupdate_slct": (By.XPATH, '/html/body/div[11]/div/div/div/div/div[2]/div/main/div/form/div[1]/div[2]/select'), 
        "registrationmethod_slct": (By.XPATH, '/html/body/div[11]/div/div/div/div/div[2]/div/main/div/form/div[2]/div[2]/select'),

        """"
        Review configuration
        """
        "product_txt": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/article[1]/div[2]/dl/div[1]/dd/div'),
        "region_txt": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/article[1]/div[2]/dl/div[2]/dd/div'),
        "reservexpiration_txt": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/article[1]/div[2]/dl/div[3]/dd/div'),
        "clusterid_txt": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/article[1]/div[2]/dl/div[4]/dd/div'),
        "baseosimg_txt": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/article[1]/div[2]/dl/div[5]/dd/div'),
        "nodecount_txt": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/article[1]/div[2]/dl/div[6]/dd/div'),
        "nodeflavor_txt": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/article[1]/div[2]/dl/div[7]/dd/div'),
        "nbaddtvdk_txt": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/article[1]/div[2]/dl/div[8]/dd/div'),
        "szaddtvdk_txt": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/article[1]/div[2]/dl/div[9]/dd/div'),
        "execyumupdt_txt": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/article[1]/div[2]/dl/div[10]/dd/div'),
        "regsrc_txt": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/main/div/article[1]/div[2]/dl/div[11]/dd/div'),

        "finish_btn": (By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/footer/button[1]')
    }