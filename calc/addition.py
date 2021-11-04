"""This is the addition calculation """

from calc.calculation import Calculation


class Addition(Calculation):
    """The addition class has one method """

    def getResult(self):
        return self.value_a + self.value_b
