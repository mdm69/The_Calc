""" content of calculator.py#"""
from calculator.main import Calculator


def test_answer():
    """Testing the multiple method of the calculator"""
    calc = Calculator()
    calc.multiple_number(10)
    assert calc.get_result() == 0
def test_spam():
    """Testing the multiple method of the calculator"""
    calc = Calculator()
    calc.multiple_number(10)
    assert calc.get_result() == 0
