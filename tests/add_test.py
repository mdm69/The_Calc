""" content of calculator.py#"""
from calculator.main import Calculator


def test_answer():
    """Testing the Add function of the calculator"""
    calc = Calculator()
    calc.add_number(6)
    assert calc.result == 6
def test_spam():
    """Testing the Add function of the calculator"""
    calc = Calculator()
    calc.add_number(6)
    assert calc.result == 6
