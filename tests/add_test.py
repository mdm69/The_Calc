""" content of calculator.py#"""
from calculator.main import Calculator


def test_answer_add():
    """Testing the Add function of the calculator"""
    calc = Calculator()
    calc.add_number(6)
    assert calc.result == 6


def test_spam_add():
    """Testing the Add function of the calculator"""
    calc = Calculator()
    calc.add_number(6)
    assert calc.result == 6
