from behave import given
from copy import deepcopy


@given(u'I create a satellite server and save the "{id_key}" id')
def step_impl(context, id_key: str):
    # Find the owner group id
    context.execute_steps('''
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an item named "rhub-admin" in the last response
    ''')

    # Create the DNS server and save the id
    satellite_req = deepcopy(
        context.api.request_data["satellite"]["server"]["create"])
    satellite_req["owner_group_id"] = context.saved_ids["group"]

    context.api.satellite.server.execute_as_admin()
    satellite_resp = context.api.satellite.server.create(**satellite_req)
    context.api.satellite.server.execute_as_test()

    satellite_resp.raise_for_status()
    satellite_id = satellite_resp.json()['id']

    context.saved_ids[id_key] = satellite_id
