from behave import given, when, then

auth = AUTH_USER = ('testuser1', 'testuser1')


@given(u'I request the token')
def step_impl(context):
    response = context.api.auth.token.create(auth)
    context.token = response.json()['access_token']

    assert(context.token != '')

    context.api.update_token(context.token)


@given(u'User is authenticated')
def step_impl(context):
    context.execute_steps(u'''
        Given I request the token
        When I execute the authentication
    ''')


@when(u'I execute the authentication')
def step_impl(context):
    # use token with random endpoint
    context.api.tower.job.get_list()


@then(u'I must have access in the system')
def step_impl(context):
    # should not throw status error
    context.api.tower.job.get_list()
