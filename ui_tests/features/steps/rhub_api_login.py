from lib2to3.pgen2 import token
from helpers import rhub_api_connection

auth = AUTH_USER = ('testuser1', 'testuser1')

token_f = rhub_api_connection.request_token(auth)


@given(u'I request the token')
def step_impl(context):
    
    assert(token_f != '')


    
@when(u'I execute the authentication')
def step_impl(context):
    resp = rhub_api_connection.request_response(context, token_f)
    assert(resp != '')


@then(u'I must have access in the system')
def step_impl(context):

    recal = rhub_api_connection.request_response(context, token_f)
    print(recal)
    assert(recal == 200)