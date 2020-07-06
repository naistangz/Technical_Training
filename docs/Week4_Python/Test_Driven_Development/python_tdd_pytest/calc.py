class Calc:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1/num2

simple_calc = Calc()
print(simple_calc.add(2, 2))
print(simple_calc.subtract(3, 1))