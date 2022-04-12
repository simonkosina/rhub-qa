@given(u'I connect to the endpoint')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I connect to the endpoint')


@when(u'I execute the authentication')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I execute the authentication')


@then(u'I must be logged in the system')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I must be logged in the system')