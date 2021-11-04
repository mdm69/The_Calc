"""This is the subtraction calculation"""

from calc.calculation import Calculation


class Multiplication(Calculation):
    """the multiplication class multiples both value a and value b """

    def getResult(self):
        """ Self is used to reference the data contained in the instance of the object which is encapsulation"""
        return self.value_a * self.value_b
