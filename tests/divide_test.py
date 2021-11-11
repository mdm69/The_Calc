"""Testing Division """
import pytest

from calculator.main import Calculator
from calculator.history.calculations import Calculations


@pytest.fixture
def clear_history():
    Calculations.clear_history()


def test_calculator_division(clear_history):
    """ tests division of two numbers """
    assert Calculator.divide_numbers(4, 2) == 2
    assert Calculator.divide_numbers(8, 2) == 4
    assert Calculator.divide_numbers(40, 10) == 4
    # Will change division factor of Zero later on
    assert Calculator.divide_numbers(1, 0) is None
    assert Calculations.history_count() == 4
    assert Calculations.get_first_history() == 2
