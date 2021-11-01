# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:
# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:
class Family():
    def __init__(self, *members, last_name):
        self.members = members
        self.last_name = last_name

# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# a method that prints all the members of the family.
    def born(self):
        self.members.append({'name':'jimmy','age':0,'gender':'Female','is_child':True})

my_family = Family({'name':'Michael','age':35,'gender':'Male','is_child':False}, "reiner")
print(my_family.members)