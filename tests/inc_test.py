""" content of calculator.py#"""
from calculator.main import Calculator


def test_answer():
    """Testing the division method of the calculator"""
    calc = Calculator()
    calc.division_number(1)
    assert calc.get_result() == 0
def test_spam():
    """Testing the division method of the calculator"""
    calc = Calculator()
    calc.division_number(1)
    assert calc.get_result() == 0
