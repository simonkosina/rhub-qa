from behave import given, when, then
from api.api import API

auth = AUTH_USER = ('testuser1', 'testuser1')

@given(u'I request the token')
def step_impl(context):
    context.api = API()

    token_f = context.api.auth.create_token(auth)
    context.token = token_f

    assert(token_f != '')

    context.api.update_token(token_f)

    
@when(u'I execute the authentication')
def step_impl(context):
    # use token with random endpoint
    context.api.tower.list_jobs()


@then(u'I must have access in the system')
def step_impl(context):
    # should not throw status error
    context.api.tower.list_jobs()
