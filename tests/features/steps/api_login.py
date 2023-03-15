import random
import string

from api_helpers import print_vars
from behave import given, when, then


@given(u'I am authenticated')
def step_impl(context):
    context.api.update_token(context.api_token)
    

@given(u'I am authenticated with an invalid token')
def step_impl(context):
    invalid_token = context.api_token
    
    while invalid_token == context.api_token:
        str_list = list(invalid_token)
        random.shuffle(str_list)
        invalid_token = ''.join(str_list)
    
    context.api.update_token(invalid_token)


@then(u'I receive an invalid token response')
def step_impl(context):
    response = context.api.me.get()
    data = response.json()

    print_vars(
        ('response.status_code', response.status_code),
        ("data['title']", data['title']),
        ("data['type']", data['type'])
    )

    assert response.status_code == 401
    assert data['title'] == 'Unauthorized'
    assert data['type'] == 'about:blank'
