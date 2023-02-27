from behave import when


@when(u'I lookup the "{kw}" id from a group named "{name}"')
def step_impl(context, kw: str, name: str):
    context.api.auth.group.get_list()

    response = context.api.logger.last_response
    response.raise_for_status()

    groups = response.json()['data']

    for group in groups:
        if group['name'] == name:
            context.saved_ids[kw] = group['id']
            break
    else:
        assert False, f'Group "{name}" doesn\'t exists.'
