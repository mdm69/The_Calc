"""Testing Addition """
import pytest

from calculator.main import Calculator
from calculator.history.calculations import Calculations

@pytest.fixture
def clear_history():
    Calculations.clear_history()


def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(10, 22) == 32
    assert Calculator.add_number(5, 6) == 11
    assert Calculator.add_number(0, 2) == 2
    assert Calculations.history_count() == 3
    assert Calculations.get_last_history() == 2
