# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:
# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:
class Family():
    def __init__(self, last_name, members = None):
        self.last_name = last_name
        if members is None:
            self.members = []
        else:
            self.members = members

    def add_members(self, member):
        if member not in self.members:
            self.members.append(member)
    

    def print_family(self):
        for member in self.members:
            print(f"Wow {member}. What a family you have!")


class Members(Family):
    def __init__(self, name, age, gender, is_child = False):
        self.name = name
        self.age = age
        self.gender = gender
        self.is_child = is_child
        # member_info = {f"'name':{self.name}, 'age': {self.age}, 'gender': {self.gender}, 'is_child' : {is_child}"}
        # self.members.append(member_info)



# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# a method that prints all the members of the family.

member1 = Members("Jeremy", 27, "Male", is_child= False)
member2 = Members("Stasia", 20, "Female", is_child= False)
family1 = Family("Reiner")
family1.add_members(member1.name)
family1.add_members(member2.name)
family1.print_family()