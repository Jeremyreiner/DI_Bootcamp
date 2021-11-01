#  Create a class called Dog with the following attributes name, age, weight.
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
dog2 = Dog("shasta", 8, 20)
dog3 = Dog("jj", 4, 35)
print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed())
dog3.fight(dog1) 