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

