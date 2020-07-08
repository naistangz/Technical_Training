# What is a dictionary in python
# An unordered collection of data values, used to store data values like a map
# Dictionary holds key:value pair
# Key value is provided in the dictionary to make it more optimised

# We use curly brackets {} to create a dictionary, separated by 'comma'

# Values in a dictionary can be of any data type and can be duplicated, whereas keys cannot be repeated and must be immutable

student_record = {
    "name": "Anais",
    "stream": "DevOps",
    "completed_lesson": 5,
    "completed_lesson_names": ["Business Skills", "SQL", "Python"]
}

# Prints out a dictionary
print(student_record)

# Prints out <class 'dict'>
finding_type = type(student_record)
print("Student record has" + str(finding_type))

# Sorts out values in alphabetical order
alpha_sorted = sorted(student_record)
print("This is the dictionary sorted in alphabetical order: " + str(alpha_sorted))

# Prints out keys
printing_keys = student_record.keys()
print("This prints out the keys: " + str(printing_keys))

# Prints out values
printing_values = student_record.values()
print("This prints out the values: " + str(printing_keys))

# Updating and replacing values within in a list
adding_subject = student_record["completed_lesson_names"] = ["Agile Methodologies", "Lists", "Data Analysis"]
print("This updates the completed_lesson_names dictionary:" + str(adding_subject))

# Locating index 1 of completed lesson names
print(student_record["completed_lesson_names"][1]) # Returns list
print(student_record["completed_lesson_names"][2]) # Returns Data Analysis

# Append new values into a list
student_record["completed_lesson_names"].append("Built-in methods")
student_record["completed_lesson_names"].append("Data Types")

# Using update to append a new key value pair in a dictionary
added_age = student_record.update({"Age": 23})
print(added_age)

# Display the list
print(student_record)




