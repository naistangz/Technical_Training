# Loops
# There two types of loops in python, for and while
# Loops iterate over a given sequence
# Loops can iterate through lists, strings, dictionaries and tuples

list_data = [1, 2, 3]

# Prints 1, 2, 3
for n in list_data:
    print(n)

# Prints out the numbers 0, 1, 2, 3, 4
for x in range(5):
    print(x)

# Combining with control flows
for data in list_data:
    if data > 4:
        break
    elif data < 0:
        print("Please enter number above 0 ")
    print(data)

# Create a string and loop through the string
city = "London"

for letter in city:
    print(letter)

# Print the string in one line
name = "Anaïs Tang"
one_line = ""

for letter in name:
    one_line += " " + letter
    if name[-1] == letter:
        print(one_line)

# Looping through a dictionary
student_record = {
    "name": "Anais",
    "stream":"Technical Consultant",
    "completed_lesson": 5,
    "completed_lesson_names": ["strings", "tuples", "variables"]
}

# iterate through values
for record in student_record.values():
    print(record)

# iterate through keys
for results in student_record.keys():
    print(results)

# iterate through items (keys and values)
for record, results in student_record.items():
    print(record, results)

# Create a dictionary with employee records minimum 5 key value pairs
employee_records = {
    "name": "Anais",
    "age": 45,
    "employee_id": 12445,
    "department": "Technology",
    "building": "C45"
}
# Using loop iterate through the dictionary
# Will output keys by default
for record in employee_records:
    print(record)

# Display the values and keys of the dictionary
for record, results in employee_records.items():
    print(record, results)


# Syntax: while variable name with condition then:
x = 1

while x < 5:
    print(f"it is working -> {x}")
    if x == 3:
        break
    x += 1
