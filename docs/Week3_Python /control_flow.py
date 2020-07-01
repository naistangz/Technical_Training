# What is control flow
# A control flow of a python is regulated by conditional statements, loops and function calls

# if, elif, else, for loop, while loop

weather = "Sunny"
conditional_weather = "rainy"

# Conditional block of code
if weather == "Snow" and conditional_weather == "rainy": # both conditions must be true
    print("let's go to the beach ")
else:
    print("sorry better luck next time")

# Using OR operator
if weather == "Snow" or conditional_weather == "rainy": # both conditions must be true
    print("let's go to the beach!")
else:
    print("sorry better luck next time")

age = 19
if age >= 18:
    print("Please proceed to checkout")
else:
    print("Sorry you are not eligible to watch this movie")

# Conditional statement exercises
# Writing a program to check these conditions by getting user input

age = int(input("How old are you?"))

if age < 21:
    print("You ain't old enough to watch this")
elif age <= 17:
    print("This is an R rated movie, unfortunately, you are underage")
elif age <= 12:
    print("You are too young to watch a PG rated film ")
else:
    print("This movie is appropriate for your age")

