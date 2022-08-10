from json import JSONDecodeError
from api.base_endpoint import BaseEndpoint
from behave import given, when, then


@when(u'development API call')
def step_impl(context):

    context.api.auth.group.get('91f74afb-a965-4acc-af13-b67bc2e5010a')
    # context.api.auth.user.get_groups('eb105ec3-6e53-47c5-ae92-a8d04912bfd8')

    print(BaseEndpoint.LOGGER.last_response.status_code)
    print()

    try:
        print(BaseEndpoint.LOGGER.last_response.json())
    except JSONDecodeError:
        print(BaseEndpoint.LOGGER.last_response.content)

    assert(False)
