import random
import string

from api_helpers import print_vars
from behave import given, when, then


@given(u'I request the token')
def step_impl(context):
    response = context.api.auth.token.create(context.auth[0], context.auth[1])
    response.raise_for_status()

    data = response.json()

    assert 'access_token' in data.keys()
    assert 'refresh_token' in data.keys()

    context.access_token = data['access_token']
    context.refresh_token = data['refresh_token']


@given(u'I request the token with invalid authentication')
def step_impl(context):
    context.api.auth.token.create('wrong name', 'wrong password')


@given(u'I am authenticated')
def step_impl(context):
    context.execute_steps(u'''
        Given I request the token
        When I update the Authorization header
    ''')


@given(u'I am authenticated with an invalid token')
def step_impl(context):
    context.execute_steps(u'''
        Given I request the token
        When I update the Authorization header
        And the access token expires
    ''')


@given(u'I am authenticated with a refreshed token')
def step_impl(context):
    context.execute_steps(u'''
        Given I am authenticated with an invalid token
        When I execute token refresh
        And I update the Authorization header
    ''')


@when(u'I update the Authorization header')
def step_impl(context):
    context.api.update_token(context.access_token)


@when(u'I update the Authorization header with an invalid token')
def step_impl(context):
    context.api.update_token('invalid token')


@when(u'the access token expires')
def step_impl(context):
    # replace token with an invalid one
    expired_token = context.access_token

    while expired_token == context.access_token:
        str_list = list(expired_token)
        random.shuffle(str_list)
        expired_token = ''.join(str_list)

    context.access_token = expired_token
    context.api.update_token(context.access_token)


@when(u'I execute token refresh')
def step_impl(context):
    response = context.api.auth.token.refresh(
        refresh_token=context.refresh_token
    )

    response.raise_for_status()

    data = response.json()

    assert 'access_token' in data.keys()
    assert 'refresh_token' in data.keys()

    context.access_token = data['access_token']
    context.refresh_token = data['refresh_token']


@then(u'I can access the API')
def step_impl(context):
    response = context.api.me.get()
    response.raise_for_status()


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


@then(u'I receive an invalid credentials response')
def step_impl(context):
    response = context.api.logger.last_response
    data = response.json()

    print_vars(
        ('response.status_code', response.status_code),
        ("data['title']", data['title']),
        ("data['type']", data['type'])
    )

    assert response.status_code == 401
    assert data['title'] == 'Unauthorized'
    assert data['type'] == 'about:blank'


@then(u'The token request fails')
def step_impl(context):
    response = context.api.logger.last_response

    assert response.status_code < 200 or response.status_code > 299

    data = response.json()

    assert 'access_token' not in data.keys()
    assert 'refresh_token' not in data.keys()
