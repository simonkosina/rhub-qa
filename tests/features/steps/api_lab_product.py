from behave import when


@when(u'I lookup the "{kw}" id from a product named "{name}"')
def step_impl(context, kw: str, name: str):
    context.api.lab.product.get_list()

    response = context.api.logger.last_response
    response.raise_for_status()

    products = response.json()['data']

    for product in products:
        if product['name'] == name:
            context.saved_ids[kw] = product['id']
            break
    else:
        assert False, f'Product "{name}" doesn\'t exists.'
