import re
import requests

from steps.api.api import filter_dict
from pprint import pformat
from textwrap import indent
from typing import Callable
from behave import given, when, then

ID_REGEXES = [
    # matches ids for /auth endpoint
    re.compile(r'.*\/([\w\d]{8}-[\w\d]{4}-[\w\d]{4}-[\w\d]{4}-[\w\d]{12})'),
    # matches integer ids
    re.compile(r'.*\/(\d+)'),
    # matches names when calling /auth/role/{role_id} endpoints
    re.compile(r'^auth\/role\/([^\/]+)$')
]


def print_vars(*args: tuple) -> None:
    """
    Prints the variable name and its corresponding value.
    """

    for var in args:
        name = var[0]
        value = var[1]

        print(f'{name}: ', end='')
        print(indent(pformat(value, sort_dicts=True), prefix='  ')[2:])
        print()


def print_request_error(error: requests.exceptions.RequestException) -> None:
    """
    Print out the details of an unsuccessful HTTP request.
    """

    content = error.response.content.decode('utf-8')
    print(f'response: {content}', end='\n\n')


def find_id_in_url(url: str) -> None | str:
    """
    Checks if the URL contains an ID parameter.
    """

    id = None

    for pattern in ID_REGEXES:
        match = re.findall(pattern, url)

        if match:
            id = match[0]  # assuming max 1 id in path

            break

    return id


def find_function_from_url(context, url: str, method: str, id: str = None) -> Callable:
    """
    Search the API objects to find a function matching
    the provided method and URL.
    """

    url_parts = url.split('/')

    if id:
        url_parts.remove(id)

    # find the object method we'll be calling
    obj = context.api

    for part in url_parts:
        obj = getattr(obj, part)

    fn = getattr(obj, method)

    return fn


def get_nested(d: dict, key_list: str):
    """
    Recursively find the nested value in the provided dictionary
    based on the keys in the list.
    """

    if len(key_list) < 1:
        raise ValueError(f'No keys provided in key_list = {key_list}.')

    if len(key_list) == 1:
        return d[key_list[0]]

    return get_nested(d[key_list[0]], key_list[1:])


@when(u'I send a "{method}" request to "{url}" endpoint')
def step_impl(context, method: str, url: str):
    id = find_id_in_url(url)
    fn = find_function_from_url(
        context,
        url,
        method,
        id
    )

    if id:
        fn(id=id)
    else:
        fn()


@when(u'test')
def step_impl(context):
    response = context.api.auth.role.get(id='rhub-admin')
    print(response.content)
    assert False


@when(u'I send a "{method}" request to "{url}" endpoint with body "{data_key}"')
def step_impl(context, method: str, url: str, data_key: str):
    id = find_id_in_url(url)
    fn = find_function_from_url(
        context,
        url,
        method,
        id
    )

    kwargs = get_nested(context.api.request_data, data_key.split('.'))

    if id:
        fn(id=id, **kwargs)
    else:
        fn(**kwargs)


@when(u'I send a "{method}" request to "{url}" endpoint with body "{data_key}" using the saved "{id_key}" id')
def step_impl(context, method: str, url: str, data_key: str, id_key: str):
    id = context.saved_ids[id_key]
    fn = find_function_from_url(
        context,
        url,
        method,
    )

    kwargs = get_nested(context.api.request_data, data_key.split('.'))

    if id:
        fn(id=id, **kwargs)
    else:
        fn(**kwargs)


@when(u'I send a "{method}" request to "{url}" endpoint using the saved "{id_key}" id')
def step_impl(context, method: str, url: str, id_key: str):
    fn = find_function_from_url(
        context,
        url,
        method
    )

    fn(id=context.saved_ids[id_key])


@when(u'I save the received "{id_key}" id')
def step_impl(context, id_key: str):
    response = context.api.logger.last_response

    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print_request_error(e)
        raise e

    if id_key == 'role':
        context.saved_ids[id_key] = response.json()['name']
    else:
        context.saved_ids[id_key] = response.json()['id']


@when(u'I use the received access token')
def step_impl(context):
    response = context.api.logger.last_response

    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print_request_error(e)
        raise e

    context.api.update_token(response.json()['access_token'])


@then(u'I receive the following response "{data_key}"')
def step_impl(context, data_key: str):
    try:
        response = context.api.logger.last_response
        response.raise_for_status()

        data = response.json()
        expected = get_nested(context.api.response_data, data_key.split('.'))

        data_filtered = filter_dict(
            data, context.api.logger.last_unverifiable_items)
        expected_filtered = filter_dict(
            expected, context.api.logger.last_unverifiable_items)

        print_vars(
            ('data_filtered', data_filtered),
            ('expected_filtered', expected_filtered)
        )

        assert data_filtered == expected_filtered

    except requests.exceptions.RequestException as e:
        print_request_error(e)
        raise e


@then(u'I receive a list of items with the following structure "{data_key}"')
def step_impl(context, data_key: str):
    try:
        response = context.api.logger.last_response
        response.raise_for_status()

        data = response.json()
        expected = get_nested(context.api.response_data, data_key.split('.'))

        expected_filtered = filter_dict(
            expected, context.api.logger.last_unverifiable_items)
        data_filtered = [filter_dict(
            x, context.api.logger.last_unverifiable_items) for x in data]

        print_vars(
            ('data_filtered', data_filtered),
            ('expected_filtered', expected_filtered)
        )

        # check if all the items match the schema
        for received in data_filtered:
            assert set(expected_filtered.keys()) == set(received.keys()
                                                        ), "Received item doesn't have the proper structure."

    except requests.exceptions.RequestException as e:
        print_request_error(e)
        raise e


@then(u'I receive a successful response')
def step_impl(context):
    try:
        response = context.api.logger.last_response
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print_request_error(e)
        raise e


@then(u'Fail and show the response')
def step_impl(context):
    try:
        response = context.api.logger.last_response
        response.raise_for_status()

        data = response.json()

        print_vars(
            ('received data', data)
        )

        assert False

    except requests.exceptions.RequestException as e:
        print_request_error(e)
        raise e
