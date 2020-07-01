# Let's create a variable

# print('Hello world')

x = 10 # type of integer
y = 3.6 # float
string = "Sparta_" # String

print(x)
print(y)
print(x + y)

# builtin method called type() to find what kind of variable it is
print(type(y))

print(str(x) + string) # you cannot combine string with an integer so turn the integer into a string

age = 99
NHS = 123455
string = 'Sparta'
salary = 50000



name = input("Please enter your name")
print(name)

# Overriding variables 
name = "james"
print(name)
name = "Christine"
print(name)

# Exercise: Capturing user details 
# Create a variable called first_name and last_name
first_name = "Kenneth"
last_name = "Leith"
print(first_name)
print(last_name)

# Create a variable called full_name and display full_name
full_name = first_name + ' ' + last_name
print(full_name)

# Create a variable called age
age = 65
print(age)

# Create a variable called address
address = "3 Tennant House"
print(address)

# Prompt the user to display all the information
print("Hello" + " " + full_name + ', ' + "you are" + " " + str(age) + " " + "years old and you live at" + " " + address)
# Returns Hello Kenneth Leith, you are 65 years old and you live at 3 Tennant House

