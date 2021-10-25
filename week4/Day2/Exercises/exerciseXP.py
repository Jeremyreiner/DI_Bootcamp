# ----------------------------------------------------------------
# Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
# ----------------------------------------------------------------
# my_favorite_numbers = set()
# my_favorite_numbers.add(1)
# my_favorite_numbers.add(2)
# # print(my_favorite_numbers)
# my_favorite_numbers.remove(2)
# # print(my_favorite_numbers)

# friends_favorite_numbers = set()
# friends_favorite_numbers.add(24)
# our_numbers = set.union(friends_favorite_numbers, my_favorite_numbers)
# print(our_numbers)
# ----------------------------------------------------------------
# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# ----------------------------------------------------------------
# tuple = (0, 1, 2)
# # tuple.add(3) #tuples cannot be changed once created. but items within can be changed
# print(tuple)

# ----------------------------------------------------------------
# Exercise 3: Print A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# ----------------------------------------------------------------
# for number in range(1,21):
#     print(number)
# ----------------------------------------------------------------
# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# ----------------------------------------------------------------
# float is a number with a decimal value, integer is a solid number with no decimal value
# integers = (1, 2, 3, 4, 5)
# for num in integers:
#     num = float(num)
#     print(num)
#     num += .5
#     print(num)
# ----------------------------------------------------------------
# Exercise 5: Shopping List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
# ----------------------------------------------------------------
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove(basket[0])
# basket.remove(basket[-1])
# basket.append("Kiwi")
# basket.append("Apple ")
# sorted(basket)
# print(sorted(basket))

# string_match = [string for string in basket if "App" in string] #returns apple and apples
# print(len(string_match))
# print(basket.clear())

# ----------------------------------------------------------------
# Exercise 6 : Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

# ----------------------------------------------------------------
# guess = True
# name = "jeremy"

# while guess:
#     user_input = input("What is your name? ")
#     if user_input == name:
#         print("Wow.. what are the odds!!")
#         break
#     else:
#         print("well, thats not my name. Try guessing my name!")
# print("incredible")

# ----------------------------------------------------------------
# Exercise 7
# Instructions
# Given a list, use a loop to print out every element which has an even index.

# ----------------------------------------------------------------
# list = []
# for nums in range(0, 11):
#     list.append(nums)
# print(list)
# odd_i = []
# even_i = []

# for i in list:
#     if i % 2 == 0:
#         even_i.append(list[i])
#     else:
#         odd_i.append(list[i])
# print(even_i)
# print(odd_i)

# ----------------------------------------------------------------
# Exercise 8
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

# ----------------------------------------------------------------
# list = []
# for nums in range(1500, 2500):
#     list.append(nums)
#     for i in list:
#         if i % 7 == 0:
#             print(i)
#         if i % 5 == 0:
#             print(i)
        
        

# ----------------------------------------------------------------
# Exercise 9: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
# ---------------------------------------------------------------

# user_input = input("Please enter a list of fruits. ")
# list_items = user_input.split()
# print(list_items)
# second_input = input("What is your favorite fruit? ")
# string_matches_list = [string for string in list_items if second_input in list_items]
# if string_matches_list:
#     print("You chose one of your favorite fruits! Enjoy!")
# else: 
#     print("You chose a new fruit. I hope you enjoy")

# ---------------------------------------------------------------
# Exercise 10: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
# ---------------------------------------------------------------
# toppings = True
# total_price = 10

# while toppings:
#     pizza_toppings = input("What toppings would you like on your pizza? ")
#     if pizza_toppings == 'quit':
#         break
#     else:
#      total_price += 2.5
     
# print(f"Your pizza will cost {total_price}")


# ---------------------------------------------------------------
# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.

# ---------------------------------------------------------------

# family_tickets = input("What are your ages?").split()
# restricted_people = []
# total_price = 0
# for age in family_tickets:
#     age = int(age)
#     if age < 3:
#         total_price += 0
#     if 3 <= age < 12:
#         total_price += 10
#     if age >= 12:
#         total_price += 15
#     if 16 <= age <= 21:
#         restricted_people.append(age)
# print(total_price)
# print(f"You are not aloud to watch this movie {restricted_people}")

# ---------------------------------------------------------------
# Exercise 12 : Who Is Under 16?
# Instructions
# Given a list of names, write a program that asks every user for their age, if they are less than 16 years old remove them from the list.
# At the end, print the final list.
# ---------------------------------------------------------------
# names = ["jeff","jimmy","jon"]
# new_list_older=[]
# for i in names:
#     age = int(input("what is your age?"))
#     if age > 16:
#         new_list_older.append(i)
# print(new_list_older)
# for name in names:
#     age.remove(new_list_older)
# print(names)


# names = ["jeff","jimmy","jon"]
# new_list_older=[]
# for i in names:
#     age = int(input("what is your age?"))
#     if age < 16:    
#         names.remove(i)


# print(names)

        

# ---------------------------------------------------------------
# Exercise 13
# Instructions
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.
# ---------------------------------------------------------------

# sandwhich_orders = ["blt", "turkey", "tuna", "ham", "cheese"] # Make a list called sandwich_orders and fill it with the names of various sandwiches .
# finished_sandwhiches =[] # Then make an empty list called finished_sandwiches.
# for i, char in enumerate(sandwhich_orders):
#     while i < len(sandwhich_orders):
#         print(f"Your {char} sandwhich is ready!")
#         finished_sandwhiches.append(char)
#         break
# print(f"All the sandwhiches are ready {finished_sandwhiches}")

# ---------------------------------------------------------------
# Exercise 14
# Instructions
# Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
# --------------------------------------------------------------

sandwhich_orders = ["blt", "turkey", "tuna", "ham", "cheese", "pastarmi", "pastarmi", "pastarmi"]
out_of = []
sandwhich = "pastarmi"
print("We are currently out of pastrami")
for i, char in enumerate(sandwhich_orders):
    # print(i, char)
    while i < len(sandwhich_orders):
        if char == "pastarmi":
            out_of.append(char)
        break
# print(out_of)
# print(sandwhich_orders)
remove = [pastarmi for pastarmi in sandwhich_orders]
for pastarmi in sandwhich_orders:
    if pastarmi in out_of:
        remove.remove(pastarmi)
print(remove)

