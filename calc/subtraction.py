"""This is the subtraction class"""

from calc.calculation import Calculation


class Subtraction(Calculation):
    """ This class subtracts value a and value b """

    def getResult(self):
        return self.value_a - self.value_b
