from .base_page import BasePage
from .main_page import MainPage
from selenium.webdriver.common.by import By

class Helpers_Page():
    
    
    def __init__(self):
        self.clusters = []
        self.arranged = []
        

    def sort_map(self, context, sorsel, line):
       

        match sorsel:
            case 'name':
                self.cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+str(ct)+']/tr[1]/td[2]/a')
                self.cluster_name = self.cluster.text

                return self.cluster_name

            case 'owner':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+str(ct)+']/tr[1]/td[3]/a')
                cluster_owner = cluster.text

                return cluster_owner

            case 'template':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+str(ct)+']/tr[1]/td[4]/a')
                cluster_template = cluster.text

                return cluster_template
            
            case 'group':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+str(ct)+']/tr[1]/td[5]/a')
                cluster_group = cluster.text

                return cluster_group

            case 'region':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+str(ct)+']/tr[1]/td[6]/a')
                cluster_region = cluster.text

                return cluster_region

            case 'status':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+str(ct)+']/tr[1]/td[7]/a')
                cluster_status = cluster.text

                return cluster_status

            case 'reservation_exp':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+str(ct)+']/tr[1]/td[8]/a')
                cluster_reserv_exp = cluster.text

                return cluster_reserv_exp
            
            case 'lifespan_exp':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+str(ct)+']/tr[1]/td[2]/a')
                cluster_life_exp = cluster.text

                return cluster_life_exp



