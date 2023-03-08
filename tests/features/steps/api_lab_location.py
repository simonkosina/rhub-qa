from behave import when


@when(u'I lookup the "{kw}" id from a location named "{name}"')
def step_impl(context, kw: str, name: str):
    context.api.lab.location.get_list()

    response = context.api.logger.last_response
    response.raise_for_status()

    locations = response.json()['data']

    for location in locations:
        if location['name'] == name:
            context.saved_ids[kw] = location['id']
            break
    else:
        assert False, f'Location "{name}" doesn\'t exists.'
