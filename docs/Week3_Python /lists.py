# Data Collection

# In python, lists are same as arrays
# Java arrays in python lists are the same as arrays
# Why List? - Manage data - access data in order - it gives
# us the option to add, remove etc.

# Syntax of list: [list] square brackets (tuple) {dictionary - key:value}
# Tuples are immutable

# Let's create a list
cities = ["Tokyo", "Paris", "Prague", "Luxembourg", "Buenos Aires"]

# display refers to (print())
print(cities)
print(type(cities)) # returns 'List'
print(cities[-1])
print(cities[1])

# Replacing indexes
cities[3] = "Amsterdam"

# Updates new list. Amsterdam has replaced Luxembourg
print(cities)

# Adds the city at the end of the string
cities.append("Vilnius")
print(cities)

# Removes Paris from the list
cities.remove("Paris")
print(cities)

# Pop removes last value from list
cities.pop()
print(cities)

# Insert adds a value to a particular index
cities.insert(2, "London")
print(cities)

# Lists with different data types
mix_type_string = [1,2,3, "one", "two", "three"]
print(mix_type_string)

string_list = ["hello", "world", "!"]
int_list = [5, 4, 3]

combined_list = string_list + int_list
print(combined_list)

# Lists within lists
combined_data_types = [[1, 2, 3], ["one", "two", "three"]]
print(combined_data_types)