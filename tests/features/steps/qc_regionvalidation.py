
from ui.pages.qccreation_form import QCCreation_form
from steps.get_attribute import GetAttribute
from behave import *
import time

@when(u'I start the provisioning but I do not select a region or the region is not available')
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

    time.sleep(2)

@then(u'I should not be able to continue to the next form page')
def step_impl(context):

    qc_form = QCCreation_form(context)
    
    assert qc_form.qcnext_btn.is_enabled() == False
    
    time.sleep(3)



@when(u'I start the provisioning and I do select a region')
def step_impl(context):
    dt_request = GetAttribute()
    
    qc_form = QCCreation_form(context)

    prd_slc = dt_request.get_data("prod_select")
    
    match prd_slc:
        case "Generic":
            qc_form.generic_rdbox.click()   
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

    qc_form.regionrdu_rdbox.click()
    time.sleep(2)


@then(u'I should be able to continue to the next form page')
def step_impl(context):
    qc_form = QCCreation_form(context)
    
    assert qc_form.qcnext_btn.is_enabled() == True
    
    time.sleep(3)