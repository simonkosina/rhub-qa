import datetime
import time

from behave import when, given
from api_helpers import get_nested
from typing import Callable


def wait_until_cluster_active(context, cluster_id: int):
    """
    Wait until the given cluster identified by it's id gets active.
    """

    while True:
        resp = context.api.lab.cluster.get(cluster_id)
        resp.raise_for_status()

        cluster = resp.json()

        if cluster["status"] == "Active":
            break
        elif "failed" in cluster["status"].lower() or "delet" in cluster["status"].lower():
            assert False, f"Error creating the '{cluster['name']}' cluster, status is '{cluster['status']}'."

        time.sleep(15)


@given(u'I save the "{cluster_name}" cluster id as "{kw}"')
def step_impl(context, cluster_name, kw):
    context.execute_steps(f'''
        When I send a "get_list" request to "lab/cluster" endpoint
        And I lookup the "{kw}" "id" from an item named "{cluster_name}" in the last response
    ''')


@given(u'a cluster with name "{name}" exists')
def step_impl(context, name):
    # check if the cluster exists already
    list_resp = context.api.lab.cluster.get_list()
    list_resp.raise_for_status()

    clusters = list_resp.json()["data"]

    for cluster in clusters:
        if cluster["name"] == name:
            return

    # setup the cluster create request
    context.execute_steps('''
        When I send a "get_list" request to "lab/product" endpoint
        And I lookup the "product" "id" from an item named "Generic" in the last response
        And I update the "product_id" item in "lab.cluster.create" using the saved "product" id
        And I send a "get_list" request to "lab/region" endpoint
        And I lookup the "region" "id" from an item named "osp_lab-pnq2-a" in the last response
        And I update the "region_id" item in "lab.cluster.create" using the saved "region" id
        And I set the expiration on cluster create request to 1h from now
    ''')

    request_args = get_nested(context.api.request_data, [
                              "lab", "cluster", "create"])
    request_args["name"] = name
    create_resp = context.api.lab.cluster.create(**request_args)

    create_resp.raise_for_status()

    cluster_id = create_resp.json()["id"]


@given(u'a cluster with name "{name}" is in active state')
def step_impl(context, name):
    # check if the cluster exists already
    list_resp = context.api.lab.cluster.get_list()
    list_resp.raise_for_status()

    clusters = list_resp.json()["data"]

    for cluster in clusters:
        if cluster["name"] != name:
            continue

        wait_until_cluster_active(context, int(cluster["id"]))

        return

    # setup the cluster create request
    context.execute_steps('''
        When I send a "get_list" request to "lab/product" endpoint
        And I lookup the "product" "id" from an item named "Generic" in the last response
        And I update the "product_id" item in "lab.cluster.create" using the saved "product" id
        And I send a "get_list" request to "lab/region" endpoint
        And I lookup the "region" "id" from an item named "osp_lab-pnq2-a" in the last response
        And I update the "region_id" item in "lab.cluster.create" using the saved "region" id
        And I set the expiration on cluster create request to 1h from now
    ''')

    request_args = get_nested(context.api.request_data, [
                              "lab", "cluster", "create"])
    request_args["name"] = name
    create_resp = context.api.lab.cluster.create(**request_args)

    create_resp.raise_for_status()

    cluster_id = create_resp.json()["id"]

    wait_until_cluster_active(context, int(cluster_id))


@when(u'I set the expiration on cluster create request to 1h from now')
def step_impl(context):
    expiration = datetime.datetime.now().astimezone(datetime.timezone.utc)
    expiration += datetime.timedelta(hours=1)

    request_args = get_nested(context.api.request_data, [
                              "lab", "cluster", "create"])
    request_args["lifespan_expiration"] = str(expiration)
    request_args["reservation_expiration"] = str(expiration)


@when(u'I find an event of type "{event_type}" in the last response and save the "{kw}" id')
def step_impl(context, event_type, kw):
    response = context.api.logger.last_response

    assert not response is None

    response.raise_for_status()

    data = response.json()

    if type(data) is dict:
        data = data['data']

    for item in data:
        assert 'type' in item.keys()

        if item['type'] == event_type:
            context.saved_ids[kw] = item['id']
            break
    else:
        assert False, f"Couldn't find an event with type '{event_type}'."


def _check_event(event: dict):
    """
    Checks whether the event dictionary has the right structure.
    """
    # Events can have two different bodies with some keys in common
    common_keys = ['_href', 'cluster_id', 'date', 'id', 'user_id', 'user_name']

    type_one_keys = set(
        common_keys + ['status', 'tower_id', 'tower_job_id', 'type'])
    type_two_keys = set(common_keys + ['new_value', 'old_value', 'type'])

    event_keys = set(event.keys())
    return event_keys == type_one_keys or event_keys == type_two_keys


@then(u'I receive a cluster event')
def step_impl(context):
    response = context.api.logger.last_response
    response.raise_for_status()

    assert _check_event(response.json())


@then(u'I receive a list of cluster events')
def step_impl(context):
    response = context.api.logger.last_response
    response.raise_for_status()

    events = response.json()

    for event in events:
        assert _check_event(event)


@then(u'I receive an event output')
def step_impl(context):
    response = context.api.logger.last_response
    response.raise_for_status()

    assert response.headers['Content-type'] == 'text/plain'
