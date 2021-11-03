# Exercise 1: Cats
# Instructions
# Using this class
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
# ---------------------------------------------------------

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# def oldest_cat(cat_list):
#     # max([cat.age for cat in cat_list])
#     return sorted(cat_list, key=lambda cat:cat.age, reverse=True)[0]

# def oldest_longer(cat_list):
#     age = cat_list[0].age
#     current_cat = cat_list[0]
#     for cat in cat_list:
#         if cat.age > age:
#             current_cat = cat
#     return current_cat


# data_list = [('rex', 34), ('mr bubbles', 12), ('meowscules', 8)]
# cats = [Cat(*data) for data in data_list]
# oldest = oldest_cat(cats)
# print(oldest.name, oldest.age)
# oldest = oldest_longer(cats)
# print(oldest.name, oldest.age)


# ---------------------------------------------------------
# Exercise 2 : Dogs
# Instructions

# Create an if statement outside of the class to check which dog is bigger.
# Print the name of the bigger dog.
# # ---------------------------------------------------------
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height.
# # This function instantiates two attributes, which values are the parameters.
# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#     # Create a method called bark that prints the following string “<dog_name> goes woof!”.
#     def bark(self):
#         print(f"{self.name} goes WOOF!!")
#     # Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”.
#     def jump(self):
#         x = self.height*2 # x is the height*2.
#         print(f"{self.name} can jump {x} cm high!!")

# # Outside of the class, create an object called davids_dog.
# # His dog’s name is “Rex” and his height is 50cm.
# davids_dog = Dog("Rex", 50)
# sarahs_dog = Dog("Teacup", 20)
# # print(davids_dog.name)
# # print(davids_dog.height)
# # davids_dog.bark()
# # davids_dog.jump()

# # print(sarahs_dog.name)
# # print(sarahs_dog.height)
# # sarahs_dog.bark()
# # sarahs_dog.jump()


# # Create an if statement outside of the class to check which dog is bigger.
# # Print the name of the bigger dog.
# data_list = [("jet", 15),("Rex", 50),("Teacup", 20)]

# def biggest_dog(data_list):
#     return sorted(data_list, key = lambda dog:dog.height)[-1]

# dogs = [Dog(*data) for data in data_list]
# biggest = biggest_dog(dogs)
# print(biggest.name)

# # ---------------------------------------------------------
# Exercise 3 : Who’s The Song Producer?
# Instructions
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

# ---------------------------------------------------------
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# class Song:
#     def __init__(self):
#         self.lyrics = {}

#     # Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
#     # Create an object, for example:
#     # stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
#     def sing_me_a_song(self):
#         song = {
#             "title": "stairway",
#             "line2": "There’s a lady who's sure",
#             "line3": "all that glitters is gold",
#             "line4": "and she’s buying a stairway to heaven"
#         }
#         self.lyrics.append(song)
#         print(song)


# Song.sing_me_a_song()

# ---------------------------------------------------------
# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list)
# and name (name of the zoo).


class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.animal_sold = []
        self.new_animal_dict = {}

    def add_animal(self, new_animal):
        '''Create a method called add_animal that takes one parameter new_animal.
        This method adds the new_animal to the animals list as long as it isn’t already in the list.'''
        animals = ["emu", "baboon", "bear",
                   "eel", "cougar", "cat", "ape", "dog"]
        for animal in animals:
            self.animals.append(animal)
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        '''Create a method called get_animals that prints all the animals of the zoo.'''
        print(
            f"Welcome to {self.zoo_name}. We currently have {len(self.animals)} animals on campus: {self.animals}")

    def sell_animal(self, animal_sold):
        '''
        This method removes the animal from the list and of course the animal needs to exist in the list.
        '''
        animal_list = []

        for i in self.animals:
            animal_list.append(i)

        for i in animal_list:
            if i == animal_sold:
                animal_list.remove(i)
                self.animals = animal_list

        print(
            f"This is the updated list of animals after selling '{animal_sold}', {self.animals}")

    # Example
    # {
    #     1: "Ape",
    #     2: ["Baboon", "Bear"],
    #     3: ['Cat', 'Cougar'],
    #     4: ['Eel', 'Emu']
    # def sorted_animals(self):
    #         return self.animals.sort()
    def sort_animals(self):
        '''Create a method called sort_animals that sorts the animals alphabetically
        and groups them together based on their first letter.'''
        sorted_classes = {
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': []
        }
        self.animals = sorted(self.animals)
        # print(f"This list has been sorted alpabetically {self.animals}")

        # Make a list for all the first letters
        list_first_letter = []
        for i in self.animals:
            if i[0] not in list_first_letter:
                list_first_letter.append(i[0])
        # print(list_first_letter)

        # Get each first letter from the list
        # Then check each animal first letter with the list of first letters
        k = 0
        for char in list_first_letter:  # for every iteration of first letter list
            k += 1
            # for every index/ animal enumerated iteration of self.animal list
            for i, animal in enumerate(self.animals):
                # if the first letter in first iteration of animal == first iteration in first letter list
                if animal[0] == char:
                    # append to sorted classes dict to row k the animals that match
                    sorted_classes[str(k)].append(animal)
        self.new_animal_dict = sorted_classes  # append the new dict to self.farm
        # print(sorted_classes)

    def get_groups(self):
        '''Create a method called get_groups that prints the animal/animals inside each group.'''
        for value in self.new_animal_dict.values():
            print(value)

    def ramat_gan_safari(self):
        '''Create an object called ramat_gan_safari and call all the methods.'''
        print(f"Welcome to {self.zoo_name}.")
        print("What animal would you like to add to the zoo? ")
        new_animal = input()
        name.add_animal(new_animal)
        name.get_animals()
        print("Which animal would you like to move from the zoo? ")
        animal_sold = input()
        name.sell_animal(animal_sold)
        name.sort_animals()
        name.get_groups()

name = Zoo("Point Defiance Zoo")
name.ramat_gan_safari()