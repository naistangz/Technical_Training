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
required_age = 18
age = int(input("How old are you?"))

if age < 18:
    print("You are too young to watch this movie.\nThe required age to watch this movie is {}".format(str(required_age)))
else:
    print("Congratulations!\nYou are old enough to watch the movie! Enjoy!")

