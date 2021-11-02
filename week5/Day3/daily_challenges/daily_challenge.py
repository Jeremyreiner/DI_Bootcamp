# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:
# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them
# ----------------------------------------------------------------
import math


class Circle:
    def __init__(self, radius, ):
        self.radius = radius
        self.list = []

    def area(self):
        return self.radius ** 2 * math.pi

    def perimeter(self):
        return 2*self.radius*math.pi

    def __le__(self, other):
        if self.radius <= other.radius:
            return True
        else:
            return False
    def __add__(self, other):
        if self.radius + other.radius:
            return self.radius + other.radius

    def add_circle(self):
        for item in self.list:
            if item not in self.list:
                self.list.append(item)

    
    def print_circle(self):
            return print(self.list)


circle = Circle(50)
circle_2 = Circle(7)
print(circle.area())
# Circle.add_circle(circle)
# Circle.add_circle(circle_2)
# Circle.print_circle()
print(circle.perimeter())
print(circle.__le__(circle_2))
print(circle.__add__(circle_2))
# bigger_circle = n_circle.area + n_circle_2.area
# print(bigger_circle.area())


# class Racecar():
#     def __init__(self, model, reg_no, top_speed=0, nitros=False):
#         self.model = model
#         self.reg_no = reg_no
#         self.top_speed = top_speed
#         self.nitros = nitros

#         if self.nitros:
#             self.top_speed += 50

#     def __str__(self):
#         return self.model.capitalize()

#     def __repr__(self):
#         return f"This is a Racecar with registration: {self.reg_no}"

#     def __call__(self):
#         print(f"Vroom Vroom. The {self.model} Engines Started")

#     def __gt__(self, other):
#         if self.top_speed > other.top_speed:
#             return True
#         else:
#             return False

#     def drive(self, km):
#         print(f"You drove the {self.model} {km} km in {km / self.top_speed} hours.")

#     def race(self, other_car):
#         if self > other_car:
#             print(f"I am the winner")
#         else:
#             print(f"The {other_car.model} is the winner")

# class PrintList():

#     def __init__(self, my_list):
#         self.mylist = my_list

#     def __repr__(self):
#         return str(self.mylist)

# car1 = Racecar("honda", "hello", 75, True)
# car2 = Racecar("civic", "bingo", 55, True)
# print(car1.__gt__(car2))
