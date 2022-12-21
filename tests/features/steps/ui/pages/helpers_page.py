import json
import time
from ui.pages.qccreation_form import QCCreation_form
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
                self.cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+line+']/tr[1]/td[2]/a')
                self.cluster_name = self.cluster.text

                return self.cluster_name

            case 'owner':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+line+']/tr[1]/td[3]/a')
                cluster_owner = cluster.text

                return cluster_owner

            case 'template':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+line+']/tr[1]/td[4]/a')
                cluster_template = cluster.text

                return cluster_template
            
            case 'group':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+line+']/tr[1]/td[5]/a')
                cluster_group = cluster.text

                return cluster_group

            case 'region':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+line+']/tr[1]/td[6]/a')
                cluster_region = cluster.text

                return cluster_region

            case 'status':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+line+']/tr[1]/td[7]/a')
                cluster_status = cluster.text

                return cluster_status

            case 'reservation_exp':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+line+']/tr[1]/td[8]/a')
                cluster_reserv_exp = cluster.text

                return cluster_reserv_exp
            
            case 'lifespan_exp':
                cluster = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+line+']/tr[1]/td[2]/a')
                cluster_life_exp = cluster.text

                return cluster_life_exp

    def get_data(self, call: str):
        
        self.f = open('./../tools/generic_conf.json', "r")
               
        data = json.loads(self.f.read())

        time.sleep(3)
        
        data_back = (data[call])
        self.f.close()


        return data_back

    def prod_selector(self, context, prodsec: str):
        qc_form = QCCreation_form(context)
        product = prodsec
        prd_slc = self.get_data(product)
    
        match prd_slc:
            case "Generic":
                qc_form.generic_rdbox.click()   #create class to select the right option based on the .json file
            case "Ceph":
                qc_form.ceph_rdbox.click()
            case "FuseKaraf":
                qc_form.fusekaraf_rdbox.click()
            case "Gluster":
                qc_form.gluster_rdbox.click()
            case "JBossEAP":
                qc_form.jbosseap_rdbox.click()
            case "OpenShift":
                qc_form.openshift_rdbox.click()
            case "OpenShift4":
                qc_form.openshift4_rdbox.click()
            case "Packstack":
                qc_form.packstack_rdbox.click()


    def cluster_walker(self, context):
        cluster_name = self.get_data("cluster_id")
    
        name_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[2]/a').text
        status_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[7]').text

        if (name_in_table != cluster_name):
    
            for i in range (1, 100, +1):
                pos_ph = str(i)
                path_table_name = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+pos_ph+']/tr[1]/td[2]/a')
                path_table_status = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+pos_ph+']/tr[1]/td[7]')

                name_in_table = path_table_name.text
                status_in_table = path_table_status.text

                if (name_in_table == cluster_name):
                    break

        else:
            print ("Cluster "+cluster_name+" not found")
            assert False

        return status_in_table