from ui.pages.main_page import MainPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from behave import *
import time

clusters = [] 
sorted_cl = []
@when(u'I navigate to the My Clusters menu')
def step_impl(context):

    main_page = MainPage(context)
    main_page.quickcluster_btn.click()
    time.sleep(1)
    main_page.mycluster_mn.click()
    time.sleep(3)


@when(u'I sort the clusters in the list by name')
def step_impl(context):

    main_page = MainPage(context)
    
    for i in range(1, 100, +1):
        try:
            cluster_name = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+str(i)+']/tr[1]/td[2]/a').text
            clusters.append(cluster_name)

        except NoSuchElementException:
            break
    

    main_page.mcnamesorting_btn.click()

    return clusters

@then(u'the clusters should be alphabetically arranged by their names')
def step_impl(context):
    
    list_cl = clusters
    for i in range(1, 100, +1):
         try:
             cluster_name = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody['+str(i)+']/tr[1]/td[2]/a').text
             sorted_cl.append(cluster_name)

         except NoSuchElementException:
             break
    
    new_list = sorted(list_cl, key=str.lower)

    assert ([i for i, j in zip(sorted_cl, new_list) if i == j])    

