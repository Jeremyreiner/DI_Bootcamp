# Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.
# ----------------------------------------------------------------------
# import math 

# class Circle():
#     def __init__(self, radius = 1.0):
#         self.radius = radius
#     def perimeter(self):
#         return (self.radius / 2) * math.pi
#     def area(self):
#         return self.radius**2 * math.pi
#     def definition(self):
#         print("This is the definition....")
# circle = Circle()
# print(circle.radius)
# print(circle.perimeter())
# print(circle.area())
# circle.definition()
# circle2 = Circle(5)
# print(circle2.radius)
# print(circle2.perimeter())
# print(circle2.area())
# circle2.definition()
# ----------------------------------------------------------------------
# Exercise 2 : Custom List Class
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist.
#  The list should be constructed with random numbers. (use list comprehension).
# ----------------------------------------------------------------------
import random
class My_list():
    def __init__(self, list = [1,6,3,4,5]):
        self.list = list
    def reverse_list(self):
        return self.list[::-1]
    def sorted_list(self):
        print(sorted(self.list))
    def new_list(self):
        new_list = []
        for i in self.list:
            new_list.append(random.randint(0, 10))
        print(new_list)
    
list = My_list()
# print(list.list)
print(list.reverse_list())
list.sorted_list()
list.new_list()