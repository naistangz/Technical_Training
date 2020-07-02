# Object Oriented Programming 

**What is OOP?**
**O**bject-**o**riented **p**rogramming **(OOP)** refers to a type of computer programming (software design) that includes or relies on the concept of classes and objects.
It is used to structure a software program into simple, reusable pieces of code or blueprints (called classes) which are used to create individual instances of objects.

**Why OOP?**
- OOP makes code organised, reusable, and easy to maintain
- Follow the DRY method (Don't Repeat Yourself)
- Prevents unwanted access to data, or exposing proprietary code through encapsulation and abstraction.

**Characteristics of objects**
* Attributes
* Behaviour

**What is a class?**
- In a class, everything is an object 
- Classes form the **blueprint** for objects
- Classes determine how data and behaviours are structured 

**What is an object?**
- An instantiation of a class
- When a class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.


**What is an instance?**


Example: 

Objects are created for specific instances of a class. You might create an animal class (blueprint) as a standard way to organise all importing information about animals, and then instantiate an individual animal as an object created from the animal class - like a fish.

## Building blocks of OOP
* Classes (blueprint)
* Objects (instances)
* Methods (behaviours)
* Attributes (data)

![oop_building_blocks](../../images/oop_class.jpg)

With a class, we can create sketches of animals with labels. It can contain details about the name, colours and size.
Based on these descriptions, we can study about each animal.

**Example 1: Creating Class and Object in Python**

```python 
class Animal:
    
    # class attribute
    species = "mammal"

    # instance attribute 
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    # instantiate the Animal class
    dog = Animal("Fluffy", 5)
    cat = Animal("Kitty", 12)

    # accessing the class attributes
    print("Fluffy is a {}.format(dog.__class__.species))
    print("Kitty is also a {}.format(cat.__class__.species))

    # accessing the instance attributes
    print("{} is {} years old".format(dog.name, dog.age))
    print("{} is {} years old".format(cat.name, cat.age))
```

Which would give the following output:

```Python
Fluffy is a mammal
Kitty is also a mammal 
Fluffy is 5 years old
Kitty is 12 years old 
```

In the above program, we created a class with the name Animal. Then, we defined the attributes. The attributes are a characteristic of an object. 

These attributes are defined inside the `__init__` method of the class. It is the initialiser method that is first run as soon as the object is created.

Then, we create instances (objects) of the `Animal` class. Here, `cat` and `dog` are references (value) to our new objects. 

We can access the class attribute using `__class__.species`. Class attributes are the same for all instances of a class. Similarly, we access the instance attributes using `dog.name` and `cat.name`. However, instance attributes are different for every instance of a class.


## Methods 

Methods are functions defined inside the body of a class. They are used to define the **behaviours** of an object. 

**Creating methods in Python**

```python 
class Animal:
    # instance attribute 
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    # instance method 
    def sound(self, sound):
        return "A {} makes a {} sound.format(self.name, song)

# instantiate the object
dog = Animal("Fluffy, 5)

# call our instance methods 
print(dog.sound("'Bark'"))
```

The output:

```python 
A dog makes a 'bark' sound
```

In the above program, we define a method `sound()`. These are called instance methods because they are called on an instance object i.e `dog`.

**`def __init__(self):`**
- This is the short form for initialising our class (creating an object)
- By using the `self` keyword we can access the attributes and methods of the class in **python**.
- It binds the attributes with the given arguments.
- This represents a constructor in Python
- We know that class is a blueprint for the objects. This blueprint can be used to create multiple numbers of objects. 

**Self can be avoided**

The object (instance) itself is passed along as the first argument, automatically. This implicit behaviour can be avoided while making a **static** method. 

```python 
class A(object):
    @staticmethod
    def stat_meth():
        print("Here, no self was passed")      
```

Here, `@staticmethod` is a function decorator which makes `stat_meth()` static.

The following code instantiates the `A` class and calls the method.

```python
>>> a = A()
>>> a.stat_meth()
Here, no self was passed
```

The implicit behaviour of passing the object as the first argument was avoided while using a static method

## Inheritance 

## Encapsulation 

## Polymorphism

## Key Points to Remember:
- OOP makes the program easy to understand as well as efficient
- The class is shareable, therefore the code can be reused.
- Data is safe and secure with data abstraction.
- Polymorphism allows the same interface for different objects, so programmers can write efficient code. 

> Exercises for OOP classes [HERE](OOP_class.py)