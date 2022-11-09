from ui.pages.qccreation_form import QCCreation_form
from steps.get_attribute import GetAttribute
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import *
import time

@when(u'I change advanced option registration method')
def step_impl(context):
    dt_request = GetAttribute()
    qc_form = QCCreation_form(context)


    prd_slc = dt_request.get_data("prod_select")
    
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

            
    time.sleep(3)

    qc_form.qcnext_btn.click()
    time.sleep(3) 

    qc_form.regionrdu_rdbox.click()  #create class to select the right option based on the .json file
    time.sleep(2)

    qc_form.qcnext_btn.click()
    time.sleep(3)
    
    qc_form.input(qc_form.clusterid_fld, dt_request.get_data("cluster_id"))

    qc_form.baseosimage_slct.click()
    time.sleep(2)

    qc_form.qcform_body.click()

    image = Select(qc_form.baseosimage_slct)
    image.select_by_visible_text(dt_request.get_data("image_select")) 
    
    time.sleep(2)

    qc_form.qcform_body.click()

    time.sleep(2)

    qc_form.nodecount_slct.send_keys((Keys.CONTROL, "a"), dt_request.get_data("node_count"))
    
    nd_flavor = Select(qc_form.nodeflavor_slct)
    nd_flavor.select_by_value(dt_request.get_data("node_flavor"))

    qc_form.input(qc_form.aditionalhd_slct, dt_request.get_data("aditionalvhd"))
    qc_form.input(qc_form.aditionalhdsize_slct, dt_request.get_data("aditionalvhdsz"))
    
    reser_days = Select(qc_form.reservationdays_slct)
    reser_days.select_by_value(dt_request.get_data("reservationdz"))
    
    qc_form.qcnext_btn.click()

    time.sleep(4)

    yum_update = Select(qc_form.yumupdate_slct) 
    yum_update.select_by_visible_text(dt_request.get_data("yumupdate"))

    time.sleep(2)

    reg_method = Select(qc_form.registrationmethod_slct)
    reg_method.select_by_visible_text(dt_request.get_data("reg_method"))

    qc_form.qcform_body.click()

    time.sleep(2)