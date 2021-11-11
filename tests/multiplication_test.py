"""Testing Multiplication """
import pytest

from calculator.main import Calculator
from calculator.history.calculations import Calculations


@pytest.fixture
def clear_history():
    Calculations.clear_history()


def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1, 9) == 9
    assert Calculator.multiply_numbers(10, 2) == 20
    assert Calculator.multiply_numbers(5, 5) == 25
    assert Calculator.multiply_numbers(20, 5) == 100
    assert Calculator.multiply_numbers(0, 2) == 0
