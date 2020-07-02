class Animal:

    def __init__(self, name=None, legNumber=None, habitat=None): # default to None, optional arguments
        self.name = name
        self.legNumber = legNumber
        self.habitat = habitat
        print("An animal has been created")


    def whoAmI(self):
        print("I am an animal")

    def eat(self):
        print("nom nom nom")

    def describe(self):
        print("{} has {} legs and lives in the {}.".format(self.name, self.legNumber, self.habitat))

    # __str__ method returns the string representation of the object
    def __str__(self):
        return "name: " + str(self.name)



Dog = Animal("Tony", 4, "house")
# Dog.setLeg(4)
print(Dog.legNumber)
Dog.describe()

# Returns the object representation
print(Dog.__repr__())

# Returns the string representation of the object
print(Dog.__str__())

"""
Difference between __str__ and __repr__ functions
__str__ must return string object whereas __repr__ can return any python expression.
If __str__ implementation is missing then __repr__ function is used as fallback. There is no fallback if __repr__ function implementation is missing.
If __repr__ function is returning String representation of the object, we can skip implementation of __str__ function.
Summary
"""
