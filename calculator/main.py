""" This is the increment function"""

def inc(x_value):
    """ Increment Function adds one to the x_value"""
    return x_value + 1

class Calculator:
    """ This is the Calculator class"""

    result = 0
    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result

    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result

    def multiple_number(self, value_a):
        """ multiple number from result"""
        self.result = self.result * value_a
        return self.result

    def division_number(self, value_a):
        """ divide number from result"""
        try:
            self.result = self.result // value_a
            return self.result
        except ZeroDivisionError:
            return None
