
# Exercise 1
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

# # ------------------------------
import datetime
# today = datetime.datetime.now()
# print(f'{today.year}/{today.day}/{today.month}')



# # ---------------------------------
# Exercise 2
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

# # ---------------------------------
# def time_to_new_years():
#     count_down = datetime.datetime(2022, 1, 1, 0, 0, 0)
#     print(count_down - today)
# time_to_new_years()
# # ---------------------------------
# Exercise 3
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then display a message stating how many minutes the user has been alive.
# # ---------------------------------

# birthdate = datetime.datetime(2022, 1, 24, 0, 0)
# def countdown():
#     today = datetime.datetime.now()
#     counter =birthdate - today
#     print(counter)
#     print(f"You are {counter.days} days to your birthday")
# countdown()
# # ---------------------------------

# Exercise 4
# Instructions
# Write a function that display today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday 
# and print which holiday that is. 
# (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.
# # ---------------------------------
# def today():
#     import datetime
#     todays_today = datetime.datetime.now()
#     holiday= datetime.datetime(2022, 1, 1)
#     date_to_h = holiday - todays_today
#     seconds = date_to_h.total_seconds()
#     min = seconds/60
#     hours = min / 60
#     print(hours + "hours")
#     print(min + "min")
#     print(seconds  + "seconds")
#     print(f'The next holiday is in: {date_to_h.days} days, {hours} hours.')
# today()




# # ---------------------------------
# Exercise 5 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.
# # ---------------------------------
# earth_year_in_secs = float(input("How old are you in seconds? "))
# planets = {
#     "Earth":  (earth_year_in_secs * 1 / 60 /60 / 24 / 365),
#     "Mercury": (earth_year_in_secs * 0.2408467) / 60/ 60/ 24 / 365,
#     "Venus": (earth_year_in_secs * 0.61519726) / 60/ 60/ 24 / 365,
#     "Mars": (earth_year_in_secs * 1.8808158) / 60/ 60/ 24 / 365,
#     "Jupiter": (earth_year_in_secs * 11.862615) / 60/ 60/ 24 / 365,
#     "Saturn": (earth_year_in_secs * 29.447498) / 60/ 60/ 24 / 365,
#     "Uranus": (earth_year_in_secs * 84.016846) / 60/ 60/ 24 / 365,
#     "Neptune": (earth_year_in_secs * 164.79132) / 60/ 60/ 24 / 365
# }
# planets = planets.items()
# for planet, time in planets:
#     print("The planet is", planet, "and you are", time, "earth-years old.")
    


# # ---------------------------------
# Exercise 6 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation 
# and learn how to properly implement faker in your code.
# Create a function that adds new dictionaries to the users list. 
# Each user has the following keys: name, adress, langage_code. 
# Use faker to populate them with fake data.
# ---------------------------------
# import Faker
# # Create an empty list called users. Tip: It should be a list of dictionaries.
# users = [
#     {'name': Faker:Name(), 'address': fake.address(), 'code language': fake.language},
#     {'name': fake.name(), 'address': fake.address(), 'code language': fake.language},
#     {'name': fake.name(), 'address': fake.address(), 'code language': fake.language},
#     {'name': fake.name(), 'address': fake.address(), 'code language': fake.language},
# ]

# def add_users():
#     print("Add new users (name, adress, langage_code): ")
#     new_user = input()
#     if new_user not in users:
#         users.append(new_user)
# add_users()


# def return_user_list():
#     print(f'this is a list of users: {users}')
# return_user_list()

# print(users)
