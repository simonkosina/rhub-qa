from behave import given, when, then
from copy import deepcopy


@given(u'I setup a user with "{num_groups}" groups and save the id')
def step_impl(context, num_groups: str):
    # Create group
    user_req = context.api.request_data["auth"]["user"]["create"]

    context.api.auth.user.execute_as_admin()
    user_resp = context.api.auth.user.create(**user_req)
    context.api.auth.user.execute_as_test()

    user_resp.raise_for_status()
    user_id = user_resp.json()['id']

    # Save the id
    context.saved_ids["user"] = user_id

    # Create users and add them to group
    for i in range(int(num_groups)):
        group_req = deepcopy(
            context.api.request_data["auth"]["group"]["create"])
        group_req["name"] = f'{group_req["name"]}{i}'

        context.api.auth.group.execute_as_admin()
        group_resp = context.api.auth.group.create(**group_req)
        context.api.auth.group.execute_as_test()

        group_resp.raise_for_status()
        group_id = group_resp.json()['id']

        context.api.auth.user.execute_as_admin()
        user_add_resp = context.api.auth.user.add_to_group(
            user_id=user_id,
            group_id=group_id
        )
        context.api.auth.user.execute_as_test()

        user_add_resp.raise_for_status()


@given(u'I setup a user with "{num_roles}" roles and save the id')
def step_impl(context, num_roles: str):
    # Create group
    user_req = context.api.request_data["auth"]["user"]["create"]

    context.api.auth.user.execute_as_admin()
    user_resp = context.api.auth.user.create(**user_req)
    context.api.auth.user.execute_as_test()

    user_resp.raise_for_status()
    user_id = user_resp.json()['id']

    # Save the id
    context.saved_ids["user"] = user_id

    # Create users and add them to group
    for i in range(int(num_roles)):
        role_req = deepcopy(
            context.api.request_data["auth"]["group"]["create"])
        role_req["name"] = f'{role_req["name"]}{i}'

        context.api.auth.role.execute_as_admin()
        role_resp = context.api.auth.role.create(**role_req)
        context.api.auth.role.execute_as_test()

        role_resp.raise_for_status()
        role_id = role_resp.json()['name']

        context.api.auth.user.execute_as_admin()
        user_add_resp = context.api.auth.user.add_to_role(
            user_id=user_id,
            role_id=role_id
        )
        context.api.auth.user.execute_as_test()

        user_add_resp.raise_for_status()


@when(u'I send a request to add user to a group using the saved ids')
def step_impl(context):
    context.api.auth.user.add_to_group(
        user_id=context.saved_ids["user"],
        group_id=context.saved_ids["group"]
    )


@when(u'I send a request to remove user from a group using the saved ids')
def step_impl(context):
    context.api.auth.user.remove_from_group(
        user_id=context.saved_ids["user"],
        group_id=context.saved_ids["group"]
    )


@when(u'I send a request to add user to a role using the saved ids')
def step_impl(context):
    context.api.auth.user.add_to_role(
        user_id=context.saved_ids["user"],
        role_id=context.saved_ids["role"]
    )


@when(u'I send a request to remove user from a role using the saved ids')
def step_impl(context):
    context.api.auth.user.remove_from_role(
        user_id=context.saved_ids["user"],
        role_id=context.saved_ids["role"]
    )
