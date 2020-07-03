from animal import Animal

# Creating a sub class of the animal class
class Reptile(Animal):
    # vertebrate = "Reptiles are vertebrates"

    def __init__(self, **kwargs):
        self.type = "Reptile" # Setting default child class type to "Reptile"
        if 'type' in kwargs: del kwargs['type'] # If Reptile is 'type' we delete it
        super().__init__(**kwargs) # using super to call the parent class initialiser with kwargs
        print("A reptile has been created")

    def whoAmI(self):
        print("I am a reptile")

Richard = Reptile()
Richard.whoAmI()










