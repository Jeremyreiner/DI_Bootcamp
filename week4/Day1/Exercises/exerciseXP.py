# Exercise 1 : Hello World
# Instructions
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# -----------------------------------------
# print("hello world " *4)

# ------------------------------------------------------------
# Exercise 2 : Some Math
# Instructions
# Write code that calculates the result of: (99^3) * 8
# ----------------------------------------------------------
# power = pow(99, 3)
# num = 8
# print(power * num)
# -------------------------------------------------------------
# Exercise 3 : What Is The Output ?
# Instructions
# Predict the output of the following code snippets:
# >>> 5 < 3
# >>> 3 == 3
# >>> 3 == "3"
# >>> "3" > 3
# >>> "Hello" == "hello"
# --------------------------------------------------------
# print(5 < 3) #false
# print(3 == 3) #true
# print(3 == '3') #false
# print('3' > 3) #cannot compare a string with a int
# print('hello' == 'Hello') #false

# --------------------------------------------------------
# Exercise 4 : Your Computer Brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
# -----------------------------------------------------------
# computer_brand = 'lenova'
# print(f'my computer brand is {computer_brand}')
# ----------------------------------------------------------
# Exercise 5 : Your Information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code
# ----------------------------------------------------------
# name = 'jeremy'
# age = 27
# shoe_size = 42
# info = f'my name is {name} and im {age} years old, as well my shoe size is {shoe_size}'
# print(info)
# ----------------------------------------------------------
# Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variables value should be a number.
# If a is bigger then b, have your code print Hello World.
# ----------------------------------------------------------
# a = input('Enter a number between one and 10: ')
# b = input('Enter a number between one and 10: ')
# if a > b:
#     print('Hello World')
# else:
#     print('Good Morning World')

# ----------------------------------------------------------
# Exercise 7 : Odd Or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

# ----------------------------------------------------------
# prompt = float(input('Please enter a number: '))
# if prompt % 2 ==0:
#     print(f'Your number {prompt} is even')
# else:
#     print(f'Your number {prompt} is odd')
# ----------------------------------------------------------
# Exercise 8 : What’s Your Name ?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
# ----------------------------------------------------------
# user_name= input('What is your name? ')
# if user_name == 'jeremy':
#     print('You and i have the same name!!')
# else:
#     print('who cares about your name....')
# ----------------------------------------------------------
# Exercise 9 : Tall Enough To Ride A Roller Coaster
# Instructions
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.
# ----------------------------------------------------------
height = float(input('What is your height in inches? '))
height_cm = height * 2.54
if (height_cm > 145):
    print(f"{height_cm} is tall enough to ride the ride")
else:
    print(f"{height_cm} is not tall enough to get on the ride")



