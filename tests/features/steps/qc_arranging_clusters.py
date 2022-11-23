import time
from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ui.pages.helpers_page import Helpers_Page
from ui.pages.main_page import MainPage

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
    helper_page = Helpers_Page
    main_page = MainPage(context)
    name_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[2]/a')

    name_sr = "name"

    cluster_name = name_in_table.text
    clusters.append(cluster_name)

    for i in range(2, 100, +1):
        line = str(i)
        try:
            cl_name = helper_page().sort_map(context, name_sr, line)
            clusters.append(cl_name)

        except NoSuchElementException:
            break
    

    main_page.mcnamesorting_btn.click()

    return clusters

@then(u'the clusters should be alphabetically arranged by their name')
def step_impl(context):
    helper_page = Helpers_Page
    name_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[2]/a')

    cl_name = name_in_table.text
    clusters.append(cl_name)
    list_cl = clusters

    for i in range(2, 100, +1):
        line = str(i)
        try:
            cl_name = helper_page().sort_map(context, "name", line)
            sorted_cl.append(cl_name)

        except NoSuchElementException:
             break
    
    new_list = sorted(list_cl, key=str.lower)

    assert ([i for i, j in zip(sorted_cl, new_list) if i == j])    


@when(u'I sort the clusters in the list by template')
def step_impl(context):
    helper_page = Helpers_Page
    main_page = MainPage(context)
    template_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[4]/a')

    name_sr = "template"

    template_name = template_in_table.text
    clusters.append(template_name)

    for i in range(2, 100, +1):
        line = str(i)
        try:
            cl_template = helper_page().sort_map(context, name_sr, line)
            clusters.append(cl_template)

        except NoSuchElementException:
            break
    
    main_page.mctemplatesoring_bnt.click()

    return clusters

@then(u'the clusters should be alphabetically arranged by their template')
def step_impl(context):
    helper_page = Helpers_Page
    template_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[4]/a')

    template_name = template_in_table.text
    clusters.append(template_name)
    list_cl = clusters

    for i in range(2, 100, +1):
        line = str(i)
        try:
            cl_template = helper_page().sort_map(context, "template", line)
            sorted_cl.append(cl_template)

        except NoSuchElementException:
             break
    
    new_list = sorted(list_cl, key=str.lower)

    assert ([i for i, j in zip(sorted_cl, new_list) if i == j])



@when(u'I sort the clusters in the list by group')
def step_impl(context):
    helper_page = Helpers_Page
    main_page = MainPage(context)
    group_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[5]/a')

    name_sr = "group"

    group_name = group_in_table.text
    clusters.append(group_name)

    for i in range(2, 100, +1):
        line = str(i)
        try:
            cl_group = helper_page().sort_map(context, name_sr, line)
            clusters.append(cl_group)

        except NoSuchElementException:
            break
    
    main_page.mcgroupsoring_bnt.click()

    return clusters


@then(u'the clusters should be alphabetically arranged by their group')
def step_impl(context, group):
    helper_page = Helpers_Page
    group_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[5]/a')

    group_name = group_in_table.text
    clusters.append(group_name)
    list_cl = clusters

    for i in range(2, 100, +1):
        line = str(i)
        try:
            cl_group = helper_page().sort_map(context, "group", line)
            sorted_cl.append(cl_group)

        except NoSuchElementException:
             break
    
    new_list = sorted(list_cl, key=str.lower)

    assert ([i for i, j in zip(sorted_cl, new_list) if i == j])

@when(u'I sort the clusters in the list by region')
def step_impl(context):
    helper_page = Helpers_Page
    main_page = MainPage(context)
    region_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[6]/a')

    name_sr = "region"

    region_name = region_in_table.text
    clusters.append(region_name)

    for i in range(2, 100, +1):
        line = str(i)
        try:
            cl_region = helper_page().sort_map(context, name_sr, line)
            clusters.append(cl_region)

        except NoSuchElementException:
            break
    
    main_page.mcregionsoring_bnt.click()

    return clusters

@then(u'the clusters should be alphabetically arranged by their region')
def step_impl(context):
    helper_page = Helpers_Page
    region_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[6]/a')

    region_name = region_in_table.text
    clusters.append(region_name)
    list_cl = clusters

    for i in range(2, 100, +1):
        line = str(i)
        try:
            cl_region = helper_page().sort_map(context, "region", line)
            sorted_cl.append(cl_region)

        except NoSuchElementException:
             break
    
    new_list = sorted(list_cl, key=str.lower)

    assert ([i for i, j in zip(sorted_cl, new_list) if i == j])

@when(u'I sort the clusters in the list by status')
def step_impl(context):
    helper_page = Helpers_Page
    main_page = MainPage(context)
    status_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[7]/a')

    name_sr = "status"
    status_name = status_in_table.text
    clusters.append(status_name)

    for i in range(2, 100, +1):
        line = str(i)
        try:
            cl_status = helper_page().sort_map(context, name_sr, line)
            clusters.append(cl_status)

        except NoSuchElementException:
            break
    
    main_page.mcstatussoring_bnt.click()

    return clusters

@then(u'the clusters should be alphabetically arranged by their status')
def step_impl(context):
    helper_page = Helpers_Page
    status_in_table = context.browser.find_element(By.XPATH, '/html/body/div/div/main/section/article/div[2]/table/tbody/tr[1]/td[7]/a')

    status_name = status_in_table.text
    clusters.append(status_name)
    list_cl = clusters

    for i in range(2, 100, +1):
        line = str(i)
        try:
            cl_status = helper_page().sort_map(context, "status", line)
            sorted_cl.append(cl_status)

        except NoSuchElementException:
             break
    
    new_list = sorted(list_cl, key=str.lower)

    assert ([i for i, j in zip(sorted_cl, new_list) if i == j])