"""The Addition Calculation"""

from calc.calculation import Calculation


class Addition(Calculation):
    """ This adds both value a and value b """

    def getResult(self):
        return self.value_a + self.value_b
