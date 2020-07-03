class Animal:
    def __init__(self, type, alive, spine, eyes, lungs, weight):
        self.type = type
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True
        self.weight = weight


    # String representation of Animal class
    def __str__(self):
        return "An animal has been created."

    def eating(self):
        print("Nom nom nom nom")

    def sleep(self):
        print({self.name} + "is sleeping zzz zzz zzz")

