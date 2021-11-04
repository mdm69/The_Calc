"""Testing Addition """


import pprint

import pytest

from calculator.main import Calculator


@pytest.fixture
def clear_history():
    Calculator.clear_history()


def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(10, 22) == 32
    assert Calculator.add_number(5, 6) == 11
    assert Calculator.add_number(0, 2) == 2
    assert Calculator.history_count() == 3
    assert Calculator.get_last_history() == 2
    pprint.pprint(Calculator.history)
