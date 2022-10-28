# FIXME: Remove this file and use the steps in the CLI tests
from behave import given, when, then


@when(u'I execute the ping API call')
def step_impl(context):
    context.api.ping.get()


@when(u'I execute the cowsay API call')
def step_impl(context):
    context.api.cowsay.get()
