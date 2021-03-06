# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.
# -----------------------------------------------------------
# def display_message():
#     print("We are trying to learn python")
# display_message()
# -----------------------------------------------------------
# Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, make sure to include a book title as an argument when calling the function.
# -----------------------------------------------------------
# def favorite_book(title):
#     print(f"My favorite book is {title}.")
# favorite_book("Alice and wonderland")
# -----------------------------------------------------------
# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the country parameter a default value.
# Call your function.
# -----------------------------------------------------------
# def describe_city(city, country = "USA"):
#     print(f"{city} is in {country}")
# describe_city("Olympia")

# -----------------------------------------------------------
# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
# -----------------------------------------------------------
# import random
# def number_range():
#     number_input = random.randint(1, 100)
#     random_num = random.randint(1, 100)
#     if number_input == random_num:
#         print(f"Your {number_input} matched with {random_num}!")
#     else:
#         print(f"Your number {number_input} is not matching the computers number {random_num}")
# number_range()
# -----------------------------------------------------------
# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function make_shirt() using positional arguments to make a shirt.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments.
# -----------------------------------------------------------
# def make_shirt(size = "L", text = "I love python"):
#     if size == "S":
#         print(f"The size of your shirt will be {size} and the message on it will be '{text}'. ")
#     elif size == "M":
#         print(f"The size of your shirt will be {size} and the message on it will be '{text}'. ")
#     elif size == "L":
#         print(f"The size of your shirt will be {size} and the message on it will be '{text}'. ")
# make_shirt()
# make_shirt("M")
# make_shirt("S", "I love boobs")




# -----------------------------------------------------------
# Exercise 6 : Magicians …
# Instructions
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the funcyion show_magicians() to see that the list has actually been modified.
# -----------------------------------------------------------
magicians = ["Randy", "David", "Glen", "Walter"]
modifier ="The great"

def show_magicians():
    for name in magicians:
        print(name)

def make_great():
    magicians = [(f"{modifier} {name}") for name in ["Randy", "David", "Glen", "Walter"]]
    print(magicians)
    
make_great()
show_magicians()

