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