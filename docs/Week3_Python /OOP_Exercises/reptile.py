from animal import Animal

# Creating a sub class of the animal class
class Reptile(Animal):
    vertebrate = "Reptiles are vertebrates"

    def __init__(self):
        super().__init__() # using super to inherit all attributes from super class, parent class (Animal)
        print("A reptile has been created")

    def whoAmI(self):
        print("I am a reptile")












