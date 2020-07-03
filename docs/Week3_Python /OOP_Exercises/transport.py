class Transport:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print("vroom vroom")

    def __repr__(self):
        print("a Transport class has been created")

Bus = Transport("Bus")
Bus.__repr__()

class Bike(Transport):
    def drive(self):
        print("brrrring brrinng") # overriding the drive method

    def __repr__(self):
        print("I am a bike")


Vanmoof = Bike("Vanmoof") # Returns brrringg bringgg
Vanmoof.drive()
Vanmoof.__repr__() # Representation of the object returns I am a bike