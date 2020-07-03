class Animal(object):

# No default values for init method
# These are values which are going to be inherited by the Reptile class
    def __init__(self, **kwargs): # unknown number of key word arguments, (state properties) # makes the function more flexible
        if 'type' in kwargs: self.type = kwargs['type'] # Checks to see if type is in argument. If so, find index of type in kwargs.
        if 'name' in kwargs: self.name = kwargs['name']
        if 'habitat' in kwargs: self.habitat = kwargs['habitat']
        print("An animal has been created")

    def type(self, t=None): # If no type of animal is given, return None as default
        if t: self.type = t # Exceptions are used to check if the value's are actually there
        try: return self.type
        except AttributeError: return None

    def name(self, n=None): # If no name is given, return None as default
        if n: self.name  = n
        try: return self.name
        except AttributeError: return None # If an error is raised when no name is given, return None

    def habitat(self, h=None): # If no habitat is given, return None as default
        if h: self.habitat = h
        try: return self.habitat
        except AttributeError: return None

    def whoAmI(self):
        print("I am an animal")

    def eat(self):
        print("nom nom nom")

    # __repr__ method returns the string representation of the object
    # def __repr__(self):
    #     print(f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".')
    #
    # # __str__ method returns the string representation of the object
    # # def __str__(self):
    # #     return "Type: " + str(self.type) + "Name:" + str(self.name) + " Habitat:" + str(self.habitat)


Dog = Animal(type="Dog", name="Rufus", sound="woof woof")
print(Dog)

#
# # Returns the object representation
# print(Dog.__repr__())
#
# # Returns the string representation of the object
# print(Dog.__str__())

"""
Difference between __str__ and __repr__ functions
__str__ must return string object whereas __repr__ can return any python expression.
If __str__ implementation is missing then __repr__ function is used as fallback. There is no fallback if __repr__ function implementation is missing.
If __repr__ function is returning String representation of the object, we can skip implementation of __str__ function.
Summary
"""
