from behave import when


@when(u'I send a request to delete a token with id "{token_id}" from a user with id "{user_id}"')
def step_impl(context, token_id: str, user_id: str):
    context.api.auth.user.delete_token(
        user_id=context.saved_ids[user_id],
        token_id=context.saved_ids[token_id]
    )


@when(u'I lookup the logged in user and save the "{kw}" id')
def step_impl(context, kw: str):
    context.execute_steps(f'''
        When I send a "get" request to "me" endpoint
        And I save the received "{kw}" id
    ''')
