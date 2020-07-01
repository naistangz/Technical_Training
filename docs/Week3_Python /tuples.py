# What is a tuple
# They are the same as lists but immutable meaning they cannot be changed
# Tuples use parenthesis
# Lists use square brackets

# Why use Tuples?
# To store data that would not need changing i.e Date of Birth, passport number, etc

# Syntax of Tuple: we use () to create a Tuple

dob = ("name", "dob", "passport number")
print(dob)

print(len(dob))
print(dob[1])

# Convert the tuple into a string
print(' '.join(dob))

# Add your name into the string at index 0
# Convert tuple into a list in order to alter
list_dob = list(dob)
new_details = list_dob.insert(0, "Anais")

# Display the list
print(list_dob)

# Turn list back to tuple
tuple_new = tuple(list_dob)
print(tuple_new)


