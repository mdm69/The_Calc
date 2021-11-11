""" This is the increment function"""

from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division
from history.calculations import Calculations


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        addition = Addition.create(value_a, value_b)
        Calculations.add_calculation_to_history(addition)
        return Calculations.get_last_history()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculations.add_calculation_to_history(subtraction)
        return Calculations.get_last_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        multiplication = Multiplication.create(value_a, value_b)
        Calculations.add_calculation_to_history(multiplication)
        return Calculations.get_last_history()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divides two numbers and store the results"""
        division = Division.create(value_a, value_b)
        Calculations.add_calculation_to_history(division)
        return Calculations.get_last_history()
