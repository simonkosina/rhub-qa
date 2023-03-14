from behave import given
from copy import deepcopy


@given(u'I create a DNS server and save the "{id_key}" id')
def step_impl(context, id_key: str):
    # Find the owner group id
    context.execute_steps('''
        Given I am authenticated
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an object named "rhub-admin" in the last response
    ''')

    # Create the DNS server and save the id
    dns_req = deepcopy(context.api.request_data["dns"]["server"]["create"])
    dns_req["owner_group_id"] = context.saved_ids['group']

    context.api.dns.server.execute_as_admin()
    dns_resp = context.api.dns.server.create(**dns_req)
    context.api.dns.server.execute_as_test()

    dns_resp.raise_for_status()
    dns_id = dns_resp.json()['id']

    context.saved_ids[id_key] = dns_id
