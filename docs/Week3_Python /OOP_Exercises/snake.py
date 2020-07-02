from reptile import Reptile

# Creating a subclass of reptile
class Snake(Reptile):

    def __init__(self): # overriding methods
        super().__init__()
        self.prey = ["mammals", "mollusks", "birds"]
        self.venom = "poisonous"
        self.body_temperature = 25
        self.eyelids = False

    def whoAmI(self):
        print("I am a snake")

    def makeSound(self):
        print("ssssss I'm a slippery slidy snaaaake")



Cobra = Snake()
Cobra.whoAmI()
Cobra.makeSound()
