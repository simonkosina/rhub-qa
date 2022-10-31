import shlex

from behave import when, then
from api.base_endpoint import BaseEndpoint


@when('I execute the "{cmd}" command')
def step_impl(context, cmd):
    context.cli.run(shlex.split(cmd))


@then('API and CLI outputs match')
def step_impl(context):
    last_response = context.api.logger.last_response
    last_unverifiable_items = context.api.logger.last_unverifiable_items

    assert(context.cli.verify(last_response, last_unverifiable_items))
