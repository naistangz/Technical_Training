# Week 3 Operators and Data types

# x = 10
# y = 11
# # x = y
# print(x == y) # Checking the values in the Boolean resulting True or False
# print(x != y) # Checking the values as Boolean resulting True or False
#
# print(x > y)
#
# print(x < y)
#
# print(x <= y)

# Let's check a real life example now to understand it better

# age = 18
#
# print(age < 19)
#
# print(3 % 9) # Modular gives the left over value of the equation

# double quotes vs single in python

# print("Hello World")
# print('Hello World')

# The best practice and why
# Using double quotes is better
# See below why

# print('Ugne's class is eng 67') # single quotes
# print("Ugne's class is eng 67") # double quote
#
# print('Anais\' class is eng 67') # single quotes
#
# # String -  casting - slicing - concatenation
#
# greeting_welcome = "Hello world"
# indexing
# H E L L O W O R L D
# 0 1 2 3 4 5 6 7 8 9
# -9               -1


# indexing = greeting_welcome.index("e") # returns index of e
# print("The index of greeting_welcome is:" + str(indexing))
#
# # Basic example of concatenation
# welcome_user = input("Please enter your name: ")
# print("Welcome " + welcome_user + "!")

# length_greeting = (len(greeting_welcome)) # to print out length of variable
# print(len(greeting_welcome))
# print("This string has " + str(length_greeting) + " characters")


# String slicing
# hi = "Hello world"
# print(hi[-1]) # d
# print(hi[1]) # e
# print(hi[0: 5]) # Hello
# print(hi[6:]) # world
# print(hi[1::2]) # start on index 1 and increment by 2 returns el ol
# print(hi[-5:]) # world

# Stripping

remove_white_space = "remove the space at the end of the string " \
                     "      "
length_white_space = len(remove_white_space)
print("Length without stripping: " + str(length_white_space))

stripping = remove_white_space.strip()
length_strip = len(stripping)
print("Length with stripping: " + str(length_strip))

# Boolean value within data types

use_text = "here is some Text with lots of text"

# Count() method counts the substring within the string
# print(use_text.count("text")) # 2
# print(use_text.count("t")) # 6

# Brings everything to lower case
print(use_text.lower()) # here is some text with lots of text
print(use_text.upper()) # HERE IS SOME TEXT WITH LOTS OF TEXT
print(use_text.capitalize()) # Here is some text with lots of text
print(use_text.islower()) # Returns boolean
print(use_text.replace("Text", "12345")) # Replaces Text with 12345
print(use_text.startswith("h")) # Returns boolean
print(use_text.title()) # Here Is Some Text With Lots Of Text

