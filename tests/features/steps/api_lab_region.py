import requests

from behave import given
from copy import deepcopy
from api_helpers import print_request_error, print_vars, filter_dict, get_nested


@given(u'I create a lab region and save the "{id_key}" id')
def step_impl(context, id_key):
    # Find existing tower, location, openstack cloud and group ids and prepare the request
    context.execute_steps('''
        When I send a "get_list" request to "tower/server" endpoint
        And I lookup the "tower" "id" from an item named "aap" in the last response
        When I send a "get_list" request to "lab/location" endpoint
        And I lookup the "location" "id" from an item named "PNQ" in the last response
        When I send a "get_list" request to "openstack/cloud" endpoint
        And I lookup the "openstack" "id" from an item named "osp_lab-pnq2-a" in the last response
        When I send a "get_list" request to "auth/group" endpoint
        And I lookup the "group" "id" from an item named "rhub-admin" in the last response
    ''')

    lab_req = deepcopy(context.api.request_data["lab"]["region"]["create"])

    lab_req["tower_id"] = context.saved_ids["tower"]
    lab_req["location_id"] = context.saved_ids["location"]
    lab_req["openstack_id"] = context.saved_ids["openstack"]
    lab_req["owner_group_id"] = context.saved_ids["group"]

    context.api.lab.region.execute_as_admin()
    lab_resp = context.api.lab.region.create(**lab_req)
    context.api.lab.region.execute_as_test()

    lab_resp.raise_for_status()

    lab_data = lab_resp.json()

    assert 'id' in lab_data.keys()

    context.saved_ids[id_key] = lab_data['id']


@when(u'I add a product with "{prod_id}" id to a region with "{reg_id}" id')
def step_impl(context, prod_id, reg_id):
    context.api.lab.region.update_products(
        region_id=context.saved_ids[reg_id],
        product_id=context.saved_ids[prod_id],
        enabled=True
    )


@when(u'I remove a product with "{prod_id}" id from a region with "{reg_id}" id')
def step_impl(context, prod_id, reg_id):
    context.api.lab.region.remove_product(
        region_id=context.saved_ids[reg_id],
        product_id=context.saved_ids[prod_id],
    )


@then(u'product with "{prod_id}" id is enabled in a region with "{reg_id}" id')
def step_impl(context, prod_id, reg_id):
    resp = context.api.lab.region.get_products(
        id=context.saved_ids[reg_id]
    )
    resp.raise_for_status()

    for product in resp.json():
        if product["product"]["id"] == context.saved_ids[prod_id]:
            assert product["product"]["enabled"] == True
            break
    else:
        assert False, "Product not found for the given region"


@then(u'product with "{prod_id}" id is disabled in a region with "{reg_id}" id')
def step_impl(context, prod_id, reg_id):
    resp = context.api.lab.region.get_products(
        id=context.saved_ids[reg_id]
    )
    resp.raise_for_status()

    for product in resp.json():
        if product["product"]["id"] == context.saved_ids[prod_id]:
            assert product["product"]["enabled"] == False


@then(u"I receive user's usage across regions")
def step_impl(context):
    try:
        response = context.api.logger.last_response
        response.raise_for_status()

        data = response.json()

        expected = get_nested(context.api.response_data, [
                              "lab", "region", "get_usage_all"])

        expected_filtered = filter_dict(
            expected, context.api.logger.last_unverifiable_items)
        usages_filtered = [filter_dict(
            x, context.api.logger.last_unverifiable_items) for x in data.values()]

        print_vars(
            ('usages_filtered', usages_filtered),
            ('expected_filtered', expected_filtered)
        )

        # check if all the items match the schema
        for usage_filtered in usages_filtered:
            assert set(usage_filtered) == set(expected_filtered)

    except requests.exceptions.RequestException as e:
        print_request_error(e)
        raise e
