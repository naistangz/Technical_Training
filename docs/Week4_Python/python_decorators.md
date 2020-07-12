# Python Decorators

## Python's Instance, Class, Static and Abstract Methods

Python offers *instance*, *class*, *static* and *abstract* methods.

```python
class Function:
    def instancemethod(self):
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
```

## **Instance Methods**
- Most widely used
- Instance method receives the instance of the class as the first argument. 
- By convention we use `self`, and refers to the instance of the class.
- `self` allows us to access the class attributes and methods on the same object.
- `self.__class__` attribute gives access to class attributes.
- **Instance methods** give us control of changing the object as well as the class state.
- `self` part of object (the instance)

Built-in example of instance method: 

```python
"hello world".capitalize()
>>> "Hello world"
```

## **Class Methods**
- Class method accepts the class as an argument
- By convention, class methods take `cls` as a parameter, which refers to the class Function instead of the object.
- Declared using `@classmethod` decorator.
- Class methods are **bound to the class** and not to the object of the class.
**Note:** They can alter the class state that would apply across all instances of class but not the object state.

Built-in example of class method:

```python
num=10
>>>num + 5
15
>>>num.__add__(5)
15
```

```python
dict.fromkey()
```

Returns new dictionary with a given sequence of elements as the keys of the dictionary

```python
dict.fromkeys('AEIOU')
{'A':None, 'E':None, 'I':None, 'O':None, 'U':None}
```

**Static Methods**
- Do not receive an implicit first argument (e.g `self` or `cls`)
- It is called a static method merely for convenience to the class object.
- It can be called from an uninstantiated class object.
**Note:** Static methods can neither modify the object state nor class state. They are primarily a way to namespace our methods.

For example:

```python
class Student(object):
    @staticmethod
    def say_hi(name):
        input = name.split(' ')
        return len(input) > 1

# Uninstantiated class object 
Student.say_hi("Anais Tang") # True
Student.say_hi("Anais") # False
```

No `self` object passed, meaning we don't have access to any instance data (attributes). This method cannot be called on an instantiated object.

**Example 2:**

```python
class Pizza(object):
    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)
```

- `mix_ingredients` is written as a static method. It can also be written as a non-static method using a `self` argument which is not used.
- Each `Pizza` object does not need to be instantiated. Bound methods are objects too, and `@staticmethod` improves readability of code when we know that is does not depend on the state of the object `Pizza` itself.
- It allows us to override the `mix_ingredients` method in a subclass. If we used a function `mix_ingredients` defined at the top-level of our module, a class inheriting from `Pizza` would not be able to change the way we mix ingredients for our pizza without overriding `cook` itself. 

## A longer example

```python
# Using static and class methods together
class ClassGrades:

    def __init__(self, grades):
        self.grades = grades

    @classmethod
    def from_csv(cls, grade_csv_str):
        grades = map(int, grade_csv_str.split(', '))
        cls.validate(grades)
        return cls(grades)


    @staticmethod
    def validate(grades):
        for g in grades:
            if g < 0 or g > 100:
                raise Exception()

try:
    # Try out some valid grades
    class_grades_valid = ClassGrades.from_csv('90, 80, 85, 94, 70')
    print 'Got grades:', class_grades_valid.grades

    # Should fail with invalid grades
    class_grades_invalid = ClassGrades.from_csv('92, -15, 99, 101, 77, 65, 100')
    print class_grades_invalid.grades
except:
    print 'Invalid!'

```

**Output:**

```python
Got grades: [90, 80, 85, 94, 70]
Invalid!
```

Static methods can work together with `from_csv` calling `validate` using the `cls` object. Running the code above prints out an array of valid grades, and then fails on the second attempt.

## Abstract Methods
- Defined in a base class, and may not provide any implementation. 

For example:

```python
class Student(object):
    def get_name(self):
        raise NotImplementedError
```

Any class inheriting from `Student` should implement and override the `get_name` method, otherwise an exception is raised.
If an inherited class from `Student` does not implement the `get_name` method, an error will be raised.

**Using the abc module**

```python
import abc

class Student(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_name(self):
        """Method that should do something"""
```

Using `abc` module and its special class when instantiating the base class `Student` or any class inheriting from it will raise a `TypeError`.

**Why do we use abstract class in Python?**
- Allows us to create functionality that subclasses (child classes) can implement or override. 
- Serves as a 'skeleton' for a subclass.
- Helpful in large code when remembering many classes is difficult.
- By declaring an abstract method in the child class, we can provide some guidelines to the child class, such that they should compulsorily implement those methods.
- If we remove the `@abstractmethod` decorator, then the method becomes a normal method and the child class may or may not give implementation to it. 

<img src = "https://cdn.educba.com/academy/wp-content/uploads/2019/10/Abstract-classes-in-Python.jpg">