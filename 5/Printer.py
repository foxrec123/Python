class Printer:
    def __init__(self):
        self.values = []

    def log(self, *values):
        self.values = [item for item in values]
        print(self.values)

class FormattedPrinter(Printer):
    def my_print(self, *values):
        print('***************************************************')
        self.log(*values)
        print('***************************************************')

instance_1 = FormattedPrinter()
instance_1.my_print('Hello my friends!', 1, 25)