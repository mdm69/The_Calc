"""Testing the Calculator"""
import pytest

from calculator.main import Calculator
from calculator.history.calculations import Calculations


@pytest.fixture
def clear_history():
    Calculations.history.clear_history()


def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculations.history_count() == 4
    assert Calculations.get_last_history() == 6


def test_clear_history(clear_history):
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculations.history_count() == 4
    assert Calculations.clear_history() == True
    assert Calculations.history_count() == 0


def test_count_history(clear_history):
    assert Calculations.history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculations.history_count() == 2


def test_get_last_calculation_result(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculations.get_last_history() == 5


def test_get_first_calculation_result(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculations.get_first_history() == 4


def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1


def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1, 2) == 2


def test_calculator_division(clear_history):
    """ tests division of two numbers """
    assert Calculator.divide_numbers(4, 2) == 2
