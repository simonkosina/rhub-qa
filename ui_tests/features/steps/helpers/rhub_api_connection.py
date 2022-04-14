import json
import random
from urllib import *
import requests
import time
import urllib3


urllib3.disable_warnings()

HOSTNAME = 'https://rhub-api-resource-hub-qe.apps.ocp-c1.prod.psi.redhat.com'
PORT = 443
PATH = '/v0'


# Specific data...
AUTH_USER = ('testuser1', 'testuser1')
auth = AUTH_USER


ENDPOINTS_ADMIN= (
    'lab/cluster',
    'scheduler/cron',
)

ENDPOINTS_USER = (
    'policies',
    'tower/job',
    'tower/server',
    'tower/template',
)

endpoints = ENDPOINTS_USER



def request_token(auth):
   
    
    i = 0
    token = ''
    while True:
        if i % 250 == 0:
            url = f"{HOSTNAME}:{PORT}{PATH}/auth/token/create"
            try:

                token_r = requests.post(url, auth=auth, timeout=2, verify=False)
                token_o = json.loads(token_r.content.decode('utf8').replace("'", '"'))
                token = token_o['refresh_token']


                return token    
                
            except Exception as e:
                print(e)
                print("Error while getting token. Ignoring...")
            time.sleep(1)

        

def request_response(context, token):
    
    url = f"{HOSTNAME}:{PORT}{PATH}/"
    target = random.choice(endpoints)

    resp = requests.get(f"{url}{target}", timeout=1, headers = {'Authorization': 'Bearer ' + token}, verify=False)

    
    return resp.status_code