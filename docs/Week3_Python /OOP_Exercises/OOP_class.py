# Create a class with key word called class
# Naming convention for creating a class is to capitalise the first letter


# Create a basic calculator inside a class
# The class should contain methods to add, subtract, divide, modulus
class Python_calculator:
    # # static method can be invoked without the need for creating an instance of a class
    # @staticmethod
    # initialising our class
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add_values(num1, num2):
        print("The sum of {} and {} is:".format(num1, num2))
        print(num1 + num2)

    def sub_values(num1, num2):
        print("The difference between {} and {} is:".format(num1, num2))
        print(num1 - num2)

    def div_values(num1, num2):
        print("{} divided by {} is: ".format(num1, num2))
        print(num1 / num2)

    def modulus_values(num1, num2):
        print("{} divided by {} gives a remainder of:".format(num1, num2))
        print(num1 % num2)

Python_calculator.add_values(5, 6)
Python_calculator.sub_values(3, 4)
Python_calculator.div_values(54, 10)
Python_calculator.modulus_values(97, 5)


