# Exercise 1 : Pets
# -------------------------------------------------------------------
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat(Pets):
#     is_lazy = False

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Char(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# # Create another cat bread. In order to do so, create a class which inherits from the Cat class.
# class HouseCat(Cat):
#     def snarl(self, sounds):
#         return f'{sounds}'


# house_an_1 = Cat("cats", 5)

# # Create a few cat instances.
# my_house_cat = HouseCat("cat", 17)
# my_bengal = Bengal("Tigger", 7)
# my_char_cat = Char("Char", 12)

# # Create a list called my_cats, which will hold all the created cat instances.
# my_cats = [my_house_cat, my_bengal, my_char_cat]

# # # Create a variable called my_pets. It’s value is an instance of the Pet class.
# # Take all the cats for a walk, use the walk method.
# my_pets = Pets(my_cats)
# my_pets.walk()
# -------------------------------------------------------------------
# Exercise 2 : Dogs
# Instructions

# -------------------------------------------------------------------
# Create a class called Dog with the following attributes name, age, weight.
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
    def bark(self):
        print(f"{self.name} is barking. BOW WOW")
    
# run_speed: returns the dogs running speed (weight/age*10).
    def run_speed(self):
        return (self.weight/ self.age) * 10

    
# fight : takes a parameter which value should be another dog called other_dog, returns a string stating which dog won the fight. 
# The winner should be the dog with the higher run_speed x weight.
    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            print(f'{self.name} has won the fight')
        else:
            print(f'{other_dog} has won the fight')


# Create 3 dogs and run them through your class.
dog1 = Dog("jet", 5, 25)
# dog2 = Dog("shasta", 8, 20)
# dog3 = Dog("jj", 4, 35)
# print(dog1.run_speed())
# print(dog2.run_speed())
# print(dog3.run_speed())
# dog3.fight(dog1) 
dog1.bark()
# -------------------------------------------------------------------
# Exercise 3 : Dogs Domesticated
# Instructions

# do_a_trick: If the dog is trained the method should print
#  one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.
# -------------------------------------------------------------------
# Exercise 3 : Dogs Domesticated
# Instructions
# ----------------------------
from exerciseXP import Dog
import random
# create a class named PetDog 
# that inherits from Dog.
class PetDog(Dog):
    # Add an attribute called trained to the __init__ method,
    #  this attribute is a boolean and the value should be False
    #  by default.

    def __init__(self, name,age, weight, trained = False):
        super().__init__(name, age, weight)
        self.name = name
        self.trained = trained
    
    # train: prints the output of bark and switches the 
    # trained boolean to True
    def trained(self, trained = True):
            return Dog.bark()

    # play: takes a parameter which value is a few names of others
    # (use *args). The method should print the following string:
    #  “dog_names all play together”.
    def play(self, *args):
        
        print(f"{self.name} are all playing together" )
    
    # do_a_trick: If the dog is trained the method should print
    #  one of the following sentences at random:
    # “dog_name does a barrel roll”.
    # “dog_name stands on his back legs”.
    # “dog_name shakes your hand”.
    # “dog_name plays dead”.
    def do_a_trick(self):
        if self.trained == True:
            tricks = [f'{self.name} does a barrel roll', f'{self.name} stands on his back legs', f'{self.name} shakes your hand', f'{self.name} plays dead']
            print(random.choices(tricks))


new_dog1 = PetDog("sheryll", 2, 10)
new_dog = PetDog("tom", 5, 20)
new_dog1.play()