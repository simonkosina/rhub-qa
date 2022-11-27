from behave import given, when, then
from copy import deepcopy


@given(u'I create a DNS server and save the "{id_key}" id')
def step_impl(context, id_key: str):
    # Create an owner group
    group_req = context.api.request_data["auth"]["group"]["create"]

    context.api.auth.group.execute_as_admin()
    group_resp = context.api.auth.group.create(**group_req)
    context.api.auth.group.execute_as_test()

    group_resp.raise_for_status()
    group_id = group_resp.json()['id']

    # Create the DNS server and save the id
    dns_req = deepcopy(context.api.request_data["dns"]["server"]["create"])
    dns_req["owner_group_id"] = group_id

    context.api.dns.server.execute_as_admin()
    dns_resp = context.api.dns.server.create(**dns_req)
    context.api.dns.server.execute_as_test()

    dns_resp.raise_for_status()
    dns_id = dns_resp.json()['id']

    context.saved_ids[id_key] = dns_id
