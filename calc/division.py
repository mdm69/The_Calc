"""This is the division calculation """

from calc.calculation import Calculation


class Division(Calculation):
    """The division class has one method """

    def getResult(self):
        try:
            return self.value_a // self.value_b
        except ZeroDivisionError:
            return None
