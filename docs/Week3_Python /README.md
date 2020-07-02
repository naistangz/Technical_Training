# Python Training :snake:

**Topics Covered In This Course:**

**Part I**
- [x] [Introduction](introduction.md)
- [x] [Data Types](variables.py)
- [x] [Strings and Concatenation](string_casting.py)
- [x] [Built-in Methods Examples](string_casting.py) 
- [x] [Importing built-in methods](importing.py) 
- [x] [More Built-in Functions with Python](https://docs.python.org/3/library/functions.html)
- [x] [Indexing And Slicing](slicing.md)
- [x] [List](lists.py)
- [x] [Dictionaries](dictionaries.py)
- [x] [Tuples](tuples.py)
- [x] [Functions](function.py)
- [x] [Variable-Length Arguments (*args, **kwargs)](kwargs.md)
- [ ] [Object-Oriented Programming] :fire:
- [x] [Control Flow](control_flow.py)
- [x] [Sets](sets.py)
- [x] [Loops](loops.py)

**Part II**
- [] Unit Testing
- [] Error Handling
- [] SQL with Python
- [] CSV and Excel Files 
- [] Using JSON with Python
- [] HTTP and APIs



## **Terminology**
**Control Flow**
- The order in which the program's code executes
- The control flow of a Python program is regulated by conditional statements, loops, and function calls

```python
# Control Flow Statements with If
required_age = 18
age = int(input("How old are you?"))

if age < 18:
    print("You are too young to watch this movie.\nThe required age to watch this movie is {}".format(str(required_age)))
else:
    print("Congratulations!\nYou are old enough to watch the movie! Enjoy!")
```
---

**Dictionary**
- An unordered collection of data values, used to store data values like a map
- Dictionary holds key:value pair
- Key value is provided in the dictionary to make it more optimised
- We use curly brackets {} to create a dictionary, separated by 'comma'
- Values in a dictionary can be of any data type and can be duplicated, whereas keys cannot be repeated and must be immutable
- Dictionaries are accessed via keys and not via their index position

```python
student_record = {
    "name": "Anais",
    "stream": "DevOps",
    "completed_lesson": 5,
    "completed_lesson_names": ["Business Skills", "SQL", "Python"]
}
```
---
**Function**
- A block of organised, reusable code that is used to perform a single, related action
- DRY *Don't* *Repeat* *Yourself*
- You can pass data (parameters), into a function.

```python
def greet(name):
    name = input("What is your name? \n")
    return "Hello, " + name + " Good morning!"
```

---
**List**
- A data structure that is mutable, or changeable.
- Each element or value that is inside of a list is called an item.
- Lists are defined by having values between square brackets []

```python
cities = ["Paris", "Hong Kong", "Buenos Aires", "London,", "Tel Aviv", "Amsterdam"]
print(cities)
```

---
**Loops**
- There are two types of loops, for and while 
- For loops can iterate over a sequence of numbers using the 'range' and 'xrange' functions
- While loops repeat as long as a certain boolean condition is met

```python
list_data = [1, 2, 3]

# Using for 
# Prints 1, 2, 3
for n in list_data:
    print(n)

# Using while
# Prints out the numbers 0, 1, 2, 3, 4
for x in range(5):
    print(x)
```

---
**Sets**
- An unordered collection data type that is iterable, mutable and has no duplicate elements
- They are very similar to lists but it has a highly optimised method for checking whether a specific element is contained in the set.
- This is based on a data structure known as a has table

```python
# Normal Set
# Prints b, c, a, d
normal_set = set(["a", "b", "c"])
normal_set.add("d")
print(normal_set)

# Frozen Set
# Prints f, e, g, cannot use 'add' attribute 
frozen_set = frozenset(["e", "f", "g"])
print(frozen_set)
```

---
**Tuple**
- They are the same as lists but immutable meaning they cannot be changed
- Tuples use parenthesis ()

```python
dob = ("name", "dob", "passport number")
print(dob)
```
---

**Variable**
- Another name for placeholder
- A reserved memory location to store data values 
- Variables can be declared by any name 
```python
this_is_variable = 19
this_is_another_variable = "Hello World"
this_is_also_a_variable = (str(this_is_variable) + this_is_another_variable)
``` 
 
> Common Python Interview Questions [HERE](https://www.guru99.com/python-interview-questions-answers.html)


