import shlex

from behave import when, then
from api.base_endpoint import BaseEndpoint


@when('I execute the "{cmd}" command')
def step_impl(context, cmd):
    context.cli.run(shlex.split(cmd))


@then('API and CLI outputs match')
def step_impl(context):
    logger = BaseEndpoint.LOGGER

    assert(context.cli.verify(logger.last_response, logger.last_unverifiable_items))
