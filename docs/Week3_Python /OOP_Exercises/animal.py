class Animal(object):

    def __init__(self, name, habitat, legNumber=0,): # default to None, optional arguments
        self.name = name
        self.habitat = habitat
        self.legNumber = legNumber
        print("An animal has been created")


    def whoAmI(self):
        print("I am an animal")

    def eat(self):
        print("nom nom nom")

    def describe(self):
        print("{} has {} legs and lives in the {}.".format(self.name, self.legNumber, self.habitat))

    # __str__ method returns the string representation of the object
    def __str__(self):
        return "Name:" + str(self.name) + " Habitat:" + str(self.habitat) + " Number of Legs:" + str(self.legNumber)


Dog = Animal("Fluff", "home", 4)
Dog.whoAmI()
Dog.eat()
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
