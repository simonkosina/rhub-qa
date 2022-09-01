from behave import given, when, then


@given(u'I request the token')
def step_impl(context):
    auth = ('testuser1', 'testuser1')
    response = context.api.auth.token.create(auth)
    response.raise_for_status()

    data = response.json()

    assert 'access_token' in data.keys()
    assert 'refresh_token' in data.keys()

    context.access_token = data['access_token']
    context.refresh_token = data['refresh_token']


@given(u'I request the token with invalid authentication')
def step_impl(context):
    auth = ('wrong name', 'wrong password')
    context.response = context.api.auth.token.create(auth)


@when(u'I execute the authentication')
def step_impl(context):
    context.api.update_token(context.access_token)


@when(u'I execute the authentication with an invalid token')
def step_impl(context):
    context.api.update_token('invalid token')


@then(u'I can access the API')
def step_impl(context):
    # should not throw status error
    response = context.api.me.get()
    response.raise_for_status()


@then(u'I must be denied access to the API')
def step_impl(context):
    response = context.api.me.get()
    
    assert response.status_code == 401

    data = response.json()

    assert data['title'] == 'Unauthorized'
    assert data['type'] == 'about:blank'


@then(u'The token request fails')
def step_impl(context):
    assert context.response.status_code < 200 or context.response.status_code > 299

    data = context.response.json()

    assert 'access_token' not in data.keys()
    assert 'refresh_token' not in data.keys()


# @given(u'User is authenticated')
# def step_impl(context):
#     context.execute_steps(u'''
#         Given I request the token
#         When I execute the authentication
#     ''')
