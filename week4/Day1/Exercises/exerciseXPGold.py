# Exercise 1 : Hello World-I Love Python
# Instructions
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python
# -----------------------------
# string1 = "hello World\n"
# string2 = "I love python\n"
# print((string1 * 4) + (string2 *4))

# -----------------------------
# Exercise 2 : What Is The Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)
# -----------------------------
month = float(input("Please give me the number of the month we are in: "))
spring = 3 <= month <= 5
summer = 6 <= month <= 8
autumn = 9 <= month <= 11
winter = month == 12 or month <= 2 and month != 0


if spring:
    print("The season is spring")
elif summer:
    print("The season is summer")
elif autumn:
    print("The season is autumn")
elif winter:
    print("The season is winter")
else:
    print("You did not answer with a valid month number")

