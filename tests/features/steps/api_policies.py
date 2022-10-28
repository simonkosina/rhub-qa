# FIXME: Remove this file and use the steps in the CLI tests
from behave import given, when, then


@when(u'I create a policy with name "{name}", department "{department}" and constraints {constraint}')
def step_impl(context, name, department, constraint):
    context.api.policies.create(name, department, constraint)


@when(u'I create a policy with name "{name}" and department "{department}"')
def step_impl(context, name, department):
    context.api.policies.create(name, department, None)


@when(u'I get a list of policies')
def step_impl(context):
    context.api.policies.get_list()
