from src.ISBN import ISBN
from behave import *
from assertpy import *
from unittest import *

use_step_matcher("re")

@given("given (?P<isbn_number>.+)")
def step_imp(context, isbn_number):
    context.isbn_class = ISBN()
    context.isbn = isbn_number

@when("the number is checked")
def step_imp(context):
    context.validation_result = str(context.isbn_class.check_number(context.isbn))


@then("the result is (?P<result>.+)")
def step_imp(context, result):
    assert_that(context.validation_result).is_equal_to(result)