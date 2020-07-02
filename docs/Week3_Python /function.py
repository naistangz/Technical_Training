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
    return "Hello, " + name + " Good morning!"

# Calling the function
print(greet())

