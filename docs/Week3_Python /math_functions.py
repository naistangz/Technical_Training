# How can we use the built in python library

from random import random
import math # importing built in modules

# Prints random numbers - mostly used in lottery
print(random())

# Round the number and selects random full number between 0 - 3
print(math.floor(random() * 3))

float_num = 24.5 # float

# Round the float number
print(math.ceil(float_num))

# Round down
print(math.floor(float_num))

# PI
print(math.pi)

# Create a method that takes two arguments
def power(a, b):
    print("{} to the power of {} is:".format(a, b))
    return math.floor((math.pow(a, b)))

print(power(3, 2))
# Returns 9

# Calculate cm into inches
# Divide cm by 2.54
def cm_to_inches(cm):
    print("cm converted into inches is:")
    return (cm/2.54)

print(cm_to_inches(9))

def cm_to_inches_select():
    select = int(input("Select a number you would like to convert: \n"))
    print("{}cm converted into inches is:".format(str(select)))
    return (select / 2.54)

print(cm_to_inches_select())
