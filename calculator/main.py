""" This is the increment function"""

from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def get_first_history():
        return Calculator.history[0].getResult()

    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_last_history():
        """ gets last value in history """
        return Calculator.history[-1].getResult()

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        Calculator.add_calculation_to_history(Addition.create(value_a, value_b))
        return Calculator.get_last_history()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        Calculator.add_calculation_to_history(Subtraction.create(value_a, value_b))
        return Calculator.get_last_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        Calculator.add_calculation_to_history(Multiplication.create(value_a, value_b))
        return Calculator.get_last_history()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divides two numbers and store the results"""
        Calculator.add_calculation_to_history(Division.create(value_a, value_b))
        return Calculator.get_last_history()