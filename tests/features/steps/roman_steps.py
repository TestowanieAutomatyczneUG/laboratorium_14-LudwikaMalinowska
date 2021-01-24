from src.Roman import RomanNumerals
from behave import *
from assertpy import *
from unittest import *

use_step_matcher("re")


#Scenario 1
@given("(?P<n>.+) is given")
def step_imp(context, n):
    context.roman_class = RomanNumerals()
    context.decimalNumber = int(n)


@then("the output is (?P<roman>.+)")
def step_imp(context, roman):
    context.romanNumber = context.roman_class.roman(context.decimalNumber)
    assert_that(context.romanNumber).is_equal_to(roman)
