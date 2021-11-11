""" calculator history """


class Calculations:

    history = []

    @staticmethod
    def get_first_history():
        return Calculations.history[0].getResult()

    @staticmethod
    def clear_history():
        Calculations.history.clear()
        return True

    @staticmethod
    def history_count():
        return len(Calculations.history)

    @staticmethod
    def add_calculation_to_history(calculations):
        Calculations.history.append(calculations)
        return True

    @staticmethod
    def get_last_history():
        """ gets last value in history """
        return Calculations.history[-1].getResult()
