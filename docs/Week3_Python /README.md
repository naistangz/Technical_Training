# Python Training :snake:

**Topics Covered In This Course:**

- [x] [Introduction](introduction.md)
- [x] [Data Types](variables.py)
- [x] [Strings and Concatenation](string_casting.py)
- [x] [Built-in Methods Examples](string_casting.py) 
- [x] [More Built-in Functions with Python](https://docs.python.org/3/library/functions.html)
- [x] [Indexing And Slicing](string_casting.py)
- [x] [List](lists.py)
- [x] [Dictionaries](dictionaries.py)
- [x] [Tuples](tuples.py)
- [ ] [Object-Oriented Programming]
- [ ] [Control Flow and Loops](control_flow.py)
- [ ] []


## **Terminology**
**Control Flow**
- The order in which the program's code executes
- The control flow of a Python program is regulated by conditional statements, loops, and function calls

```python
# Control Flow Statements with If
age = int(input("How old are you?"))

if age < 21:
    print("You ain't old enough to watch this")
elif age <= 17:
    print("This is an R rated movie, unfortunately, you are underage")
elif age <= 12:
    print("You are too young to watch a PG rated film ")
else:
    print("This movie is appropriate for your age")
```

**Dictionary**
- An unordered collection of data values, used to store data values like a map
- Dictionary holds key:value pair
- Key value is provided in the dictionary to make it more optimised
- We use curly brackets {} to create a dictionary, separated by 'comma'
- Values in a dictionary can be of any data type and can be duplicated, whereas keys cannot be repeated and must be immutable

```python
student_record = {
    "name": "Anais",
    "stream": "DevOps",
    "completed_lesson": 5,
    "completed_lesson_names": ["Business Skills", "SQL", "Python"]
}
```

**Tuple**
- They are the same as lists but immutable meaning they cannot be changed
- Tuples use parenthesis ()

```python
dob = ("name", "dob", "passport number")
print(dob)
```

**List**
- A data structure that is mutable, or changeable.
- Each element or value that is inside of a list is called an item.
- Lists are defined by having values between square brackets []

```python
cities = ["Paris", "Hong Kong", "Buenos Aires", "London,", "Tel Aviv", "Amsterdam"]
print(cities)
```
---

> Common Python Interview Questions [HERE](https://www.guru99.com/python-interview-questions-answers.html)


