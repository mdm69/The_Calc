"""This is the Division class"""

from calc.calculation import Calculation


class Division(Calculation):
    """ This class divides value a and value b """

    def getResult(self):
        try:
            return self.value_a // self.value_b
        except ZeroDivisionError:
            return None
