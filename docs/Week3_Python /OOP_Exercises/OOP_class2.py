class Animal:
    # class variable outside functions - dangerous
    animal_kind = "canine"

    def __init__(self, name, colour, breed, hunger):
        self.name = name
        self.colour = colour
        self.breed = breed
        self.hunger = hunger

    def bark(self):
        self.animal_kind
        return "woof woof"

    def sleep(self):
        return "zzz zzz zzz"

    def run(self):
        return "walkies!"

    def eat(self):
        return "nom nom nom..."

pip = Animal("Pip", "white", "Labrador", hunger="hungry") # creating an object of our class
print(pip.name) # printing an attribute
print(pip.colour)
print(pip.animal_kind)

kiko = Animal("Kiko", "brown", "Poodle", hunger="starving") # instantiating or creating an object
print(kiko.colour)
print(kiko.name)
print(kiko.bark())

mongoose = Animal("Mongoose", "black", "Yorkshire Terrior", hunger="hungry")
print(mongoose.run())
print(mongoose.eat())
print(mongoose.breed)

mika = Animal("Mika", "pink", "German Shepherd", hunger="hungry")
mika.animal_kind = "fish"
print(mika.animal_kind)

# Using Inheritance
class Bird(Animal):
    # def __init__(self):
    #     # super inherits everything from Animal class
    #     super().__init__()
    #     print("I am a  bird!")

    def tweet(self):
        print("tweet tweet")

    def eat(self):
        print("nibble nibble")

    def info(self):
        print(f"I am a bird. My name is {self.name}. I am a {self.breed}")


richard = Bird("Richard", "blue", "blue tit", hunger="starving")
richard.tweet()
richard.eat()

