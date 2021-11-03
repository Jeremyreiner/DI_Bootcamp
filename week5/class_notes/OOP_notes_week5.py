# ----------------------OOP WEEK5 DAY 1---------------------------------------------------------
# syntax of class needs capital letter after class
# functions inside of a class are methods
# a function outside of a class is a function
# class Dog():
#     # when introducing classes always use self first
#     # then each attribute follows, ie name, legs
#     def __init__(self, name, height,  age,  walks,  jumps,  sleeps,):
#             self.name = name
#             self.height = height
#             self.age = age
#             self.walks = walks
#             self.jumps = jumps
#             self.sleeps = sleeps
#     def behavior(self):
#         print(f"{self.name} Im barking.... woof")
#     def introduce(self):
#         #  usage of self like this.target in js introduces new objects according
#         # according to themselves making the code responsive
#         print(f"My dogs name is {self.name}, he is {self.height} and is {self.age} years old")
#         print(f"he can {self.walks}, but cannot {self.jumps} and {self.sleeps}")


# # creation of obj1 and giving them parameters that
# # fill the methods parameters
# dog1 = Dog("Tom", 4, 9, "walk", "Cannot jump", "sleeps all the time")
# #creation of obj2 and giving them parameters that
# # fill the methods parameters
# dog2 = Dog("Jerry", 1, 2, "walk", "jump", "sleeps all the time")

# dog2.introduce()
# dog2.behavior()
# dog1.introduce()
# -----------------------------------
# class Point():

#     # init and self bring the class alive and after self brings
#     # each attribute of itself, the new item. Which has
#     # attributes x and y
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# # create an instance of the class
# # and givve the paramaters an argument
# # for x and y
# p = Point(3,4)

# print("p.x is:", p.x)
# print("p.y is:", p.y)
# -----------------------------------------------------------
# # creates class object person
# class Person():
#   def __init__(self, name, age): #giving parameters to the class object
#     self.name = name
#     self.age = age

#   def show_details(self): #calling the class and printing a string with the classes new name
#     print("Hello my name is " + self.name)

# first_person = Person("John", 36)
# first_person.show_details() #show details calls the value of self.name and returns the string plus self.name
# ---------------------------------------------------------------------
# class BankAccount:
# class Bank_account():
#     def __init__(self, account_number, balance=150):
#         self.account_number = account_number
#         self.balance = balance
#         self.transactions = []

#     def view_balance(self):
#         self.transactions.append("View Balance")
#         print(f"Balance for account {self.account_number}: {self.balance}")

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#         elif amount < 100:
#             print("Minimum deposit is 100")
#         else:
#             self.balance += amount
#             self.transactions.append(f"Deposit: {amount}")
#             print("Deposit Succcessful")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient Funds")
#         else:
#             self.balance -= amount
#             self.transactions.append(f"Withdraw: {amount}")
#             print("Withdraw Approved")
#             return amount

#     def view_transactions(self):
#         print("Transactions:")
#         print("-------------")
#         for transaction in self.transactions:
#             print(transaction)
# person = Bank_account(123456)
# print(Bank_account)
# ----------------------DAY 2---- INHERITING CLASSES-------------------------------------------
# class Animal():
#     def __init__(self, name, legs):
#         self.name = name
#         self.legs = legs
#     def walks(self):
#         if self.legs:
#             print(f"The animal {self.name} walks on {self.legs} legs")
#         else:
#             print(f"{self.name} has no legs....")

# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} meowed. per...")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} barked, WAF")

# animal = Animal('frog', 10)
# cat = Cat('cat', 4)
# dog = Dog('rex', 4)
# # dog.bark()
# # cat.meow()
# # dog.walks()
# # animal.walks()
# # cat.walks()
# # print(isinstance(dog, Dog)) #True
# # print(isinstance(Dog, Animal)) #False
# print(dog.name)
# ---------------------------------------------------------------------
# # Try to recreate the class explained below:
# import random
# # We have a class called Door that has an attribute of is_opened declared when an instance is initiated.


# class Door():
#     door_string = 'door has been'
#     def __init__(self):
#         self.is_opened = random.choice([False, True])

#     def open_door(self):
#         self.is_opened == True
#         print(self.door_string + " opened")

#     def closed_door(self):
#         self.is_opened == False
#         print(self.door_string + " closed")

# # We can create a class called BlockedDoor that inherits from the base class Door.
# # We just override the parent class's functions of open_door()
# #  and close_door() with our own BlockedDoor version of those functions,
# #   which simply raises an Error that a blocked door cannot be opened or closed.


# class BlockedDoor(Door):
#     def open_door(self):
#         print("A  blocked door cannot be oppened")

#     def closed_door(self):
#         self.open_door()


# door = Door()
# blocked_door = BlockedDoor()

# # door.open_door()
# # door.closed_door()

# blocked_door.open_door()
# blocked_door.closed_door()

# ---------------------------------------------------------------------
# class Computer():

#     def __init__(self):
#         self.name = "Apple Computer" # public
#         self.__max_price = 900 # private

#     def sell(self):            # public method
#         print(f"Selling Price: {self.__max_price}")

#     def __sell(self):          # private method
#       print('This is private method')

#     def set_max_price(self, price):
#         self.__max_price = price

# c = Computer()

# c.sell()

# c.__sell()
# ---------------------------------------------------------------------

# class Parrot():

#     def fly(self):
#         print("Parrot can fly")

#     def swim(self):
#         print("Parrot can't swim")

# class Penguin():

#     def fly(self):
#         print("Penguin can't fly")

#     def swim(self):
#         print("Penguin can swim")

# # common interface
# def flying_test(bird):
#     bird.fly()

# #instantiate objects
# blu = Parrot()
# peggy = Penguin()

# # passing the object
# flying_test(blu)
# # >> Parrot can fly

# flying_test(peggy)
# # >> Penguin can't fly
# ---------------------------------------------------------------------
# class A():

#     def dothis(self):
#         print("doing this in A")


# class B(A):
#     pass


# class C():
#     def dothis(self):
#         print("doing this in C")


# class D(B, C):          #To access another class, swap the parameter positions. This instance B is the alpha parameter
#     pass                #while everything after is the beta parameter

# d_instance = D()        #instance D returns the class a dothis method
# d_instance.dothis()     #Prints class A


# ---------------------------------------------------------------------
# class Book():
#     def __init__(self, title, author, publication_date, price):
#         self.title = title
#         self.author = author
#         self.publication = publication_date
#         self.price = price

#     def present(self):
#         print(f'Title: {self.title}')

# class Fiction(Book):
#     def __init__(self, title, author, publication_date, price, is_awesome):
#         super().__init__(title, author, publication_date, price)
#         self.genre = 'Fiction'
#         self.is_awesome = is_awesome
#         if self.is_awesome:
#             self.bored = False
#             print('Woow this is an awesome book')
#         else:
#             self.bored = True
#             print('I am very bored')

# if __name__ == '__main__':
#     foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
#     foundation.present()
#     print(foundation.price)
#     print(foundation.bored)
#     boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
#     print(boring_book.bored)

# ---------------------------------------------------------------------
# class Alien():
#     def __init__(self, name, planet):
#         self.name = name
#         self.planet = planet

#     def fly(self):
#         print(self.name, 'is flying!')

#     def sleep(self):
#         print("Aliens don't sleep")

# class Animal():
#     def __init__(self, name):
#         self.name = name

#     def sleep(self):
#         print("zzzZZZZZ")

# class Dog(Animal):
#     def bark(self):
#         print("{} barked, WAF !".format(self.name))

# class AlienDog(Alien, Dog):
#     def bark(self):
#         print("{} barked, 0ul10ul0u (that's how aliens dogs bark..) !".format(self.name))


# my_normal_dog = Dog("Roger")    #Dog activitates class animal and is given a name
# my_normal_dog.sleep()           #inside animals can sleep 
# my_normal_dog.bark()            #inside of dogs dogs can bark
# my_alien_dog = AlienDog("Rex", "Neptune")   #aliens take name and planet arguments
# print(my_alien_dog.planet)      #alienDog accepts the classes of alien and dog(Which also has animal class)
# my_alien_dog.fly()              #fly is taken from alien class and accepted within alien dog class
# my_alien_dog.sleep()            #sleep comes from the animal class which is activated inside of the dog class
# my_alien_dog.bark()             #bark comes from the animal class which is activated inside of the dog class