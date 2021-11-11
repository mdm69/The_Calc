"""This is Abstract Class"""


class Calculation:
    """ the constructors"""

    def __init__(self, value_a, value_b):
        """ This is the instance property  """
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """ Class Method makes it bound to the class and not the instance """
        return cls(value_a, value_b)
