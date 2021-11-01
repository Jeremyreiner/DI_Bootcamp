# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output!
# File: market.py
# Create the code that is needed to recreate the code provided above. Below are a few questions to assist you with your code:
# 1. Create a class called Farm. How should this be implemented?
# 2. Does the Farm class need an __init__ method? If so, what parameters should it take?
# 3. How many methods does the Farm class need?
# 4. Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# 5. Test your code and make sure you get the same results as the example above.
# 6. Bonus: nicely line the text in columns as seen in the example above. Use string formatting.


class Farm():
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.sorted_animals = []

    def add_animal(self, animal, amount = ""):
        if animal not in self.animals:
            added_animal = f"{animal} : {str(amount)}"
            self.animals.append(added_animal)
        

    def show_animals(self):
        # for animal in self.animals:
        print(f"These animals are currently in {self.name}'s farm: {self.animals}")
    

# Expand The Farm
# Add a method called get_animal_types to the Farm class. 
# This method should return a sorted list of all the animal types (names) in the farm. 
# With the example above, the list should be: ['cow', 'goat', 'sheep'].
    def get_animal_types(self):
        if __name__ == '__main__':
            sorted_by_name = sorted(self.animals, key=lambda x: x.animals)
            print(sorted_by_name)

        




# Add another method to the Farm class called get_short_info. 
# This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. 
# The method should call the get_animal_types function to get a list of the animals.



macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.show_animals()
all_animals = macdonald.animals
macdonald.get_animal_types()
# print(macdonald.get_info())

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!