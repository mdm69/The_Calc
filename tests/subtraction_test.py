"""Testing Multiplication """
import pytest

from calculator.main import Calculator
from calculator.history.calculations import Calculations


@pytest.fixture
def clear_history():
    Calculations.clear_history()


def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(4, 2) == 2
    assert Calculator.subtract_number(1, 10) == -9
    assert Calculator.subtract_number(1, 1) == 0
    assert Calculator.subtract_number(10, -2) == 12
