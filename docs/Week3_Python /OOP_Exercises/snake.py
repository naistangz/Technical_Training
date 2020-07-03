from reptile import Reptile

# Creating a subclass of reptile
class Snake(Reptile):

    def __init__(self, **kwargs): # overriding methods
        self.type = "Snake"
        if "type" in kwargs: del kwargs['type']
        super().__init__(**kwargs)
        # self.prey = ["mammals", "mollusks", "birds"]
        # self.venom = "poisonous"
        # self.body_temperature = 25
        # self.eyelids = False

    def whoAmI(self):
        print("I am a snake")

    # def print_animal(o):
    #     if not isinstance(o, Animal):
    #         raise TypeError('print_animal(): requires an Animal')
    #     print(f'The{o.type()} is named "{o.name()}"and can be found in"{o.habitat()} "and says "{o.sound()}".')
    # # Printing info about snakes
    # def main():
    #     Cobra = Snake(name= "Donald", sound="ssssss I'm a slippery slidy snaaaake")
    #     print_animal(Cobra)

    # if __name__ == "__main__": main()

Cobra = Snake()
Cobra.whoAmI()