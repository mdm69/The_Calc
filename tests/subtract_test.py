""" content of calculator.py#"""
from calculator.main import Calculator


def test_answer():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(5)
    assert calc.get_result() == -5
def test_spam():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(5)
    assert calc.get_result() == -5
