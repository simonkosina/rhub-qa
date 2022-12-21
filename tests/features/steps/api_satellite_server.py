from behave import given, when, then
from copy import deepcopy


@given(u'I create a satellite server and save the "{id_key}" id')
def step_impl(context, id_key: str):
    # Create an owner group
    group_req = context.api.request_data["auth"]["group"]["create"]

    context.api.auth.group.execute_as_admin()
    group_resp = context.api.auth.group.create(**group_req)
    context.api.auth.group.execute_as_test()

    group_resp.raise_for_status()
    group_id = group_resp.json()['id']

    # Create the DNS server and save the id
    satellite_req = deepcopy(
        context.api.request_data["satellite"]["server"]["create"])
    satellite_req["owner_group_id"] = group_id

    context.api.satellite.server.execute_as_admin()
    satellite_resp = context.api.satellite.server.create(**satellite_req)
    context.api.satellite.server.execute_as_test()

    satellite_resp.raise_for_status()
    satellite_id = satellite_resp.json()['id']

    context.saved_ids[id_key] = satellite_id
