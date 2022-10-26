from ui.pages.qccreation_form import QCCreation_form
from steps.get_attribute import GetAttribute
from behave import *
import time

@when(u'I start the quick cluster provisioning but not satisfy the cluster name policy')
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
    
    qc_form.input(qc_form.clusterid_fld, "Teste 001")

    qc_form.qcform_body.click()
    

@when(u'I start the quick cluster provisioning and satisfy the cluster name policy')
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

    qc_form.qcform_body.click()