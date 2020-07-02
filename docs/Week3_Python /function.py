# Python Functions
# A function is a group of related statements that performs a specific task
# Functions help break our program into smaller and modular chunks.
# As our program grows larger and larger, functions make it more organised and manageable
# DRY don't repeat yourself. It avoids repetition and makes the code reusable.

# Syntax of function

def function_name(parameters):
    """docstring"""
    statement(s)

# Keyword def marks start of the function header
# A function name to uniquely identify the function
# Function naming follows the same rules of writing identifiers in Python
# Parameters(arguments) through which we pass values to a function. They are optional.
# A colon (:) to mark the end of the function header.
# Optional doc string(docstring) to describe what the function does.
# Optional return statement to return a value from the function

# pass is used to skip the function
# it is used in creating or building a unit test
def test():
    pass


def hello():
    return "Hello World"

# Calling the function
print(hello())

def greet():
    name = input("What is your name? \n")
    return "Hello " + name + ", I hope you are having a good morning!"

# Calling the function
print(greet())

def greet():
    name = input("What is your name? \n")
    print("Hello, " + name + " Good morning!")
# Using print will return None. We require return in order for the function to give back a value

# We can return anything - string or int with + operator
# This function tells us that there are two arguments involved
def add_values(a, b):
    print("The sum of these values are:")
    return a + b

# If we do not enter two arguments, it was pass an error
print(add_values(4, 5))
print(add_values(5, 6))

# Creating a function to return subtraction
def sub_values(a, b):
    print("The difference between these values are:")
    return a - b

print(sub_values(15045, 2342))
print(sub_values(56, 3))

# Creating a function to return division
def divide(a, b):
    print("The division between the values is")
    return a / b

print(divide(10, 2))
print(divide(324,5))

# Creating a function to return multiplication
def multiply(a, b):
    print("The product of these values are:")
    return a * b

print(multiply(5, 6))
print(multiply(4, 198))

# Create a function to find the remainder
def modulus(a , b):
    print("The remainder of the values is:")
    return a % b

print(modulus(100, 4))
print(modulus(45, 7))

# Adding user input
def user_multiply():
    num_1 = int(input("Choose a number:\n"))
    num_2 = int(input("Choose another number:\n"))
    print("The product of your chosen numbers is: ")
    return num_1 * num_2

print(user_multiply())


# Creating a function with multiple args
def multi_args(*kwargs):
    print(type(kwargs))

    for args in kwargs:
        print(args)
    return args

print(multi_args(1, 2, 4, 6, 7))