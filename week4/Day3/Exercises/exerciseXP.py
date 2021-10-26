# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# ---------------------------------------------------------------
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dictonary = dict(zip(keys, values))
# print(dictonary)
# ---------------------------------------------------------------
# Exercise 2 : Cinemax #2
# Instructions
# “Continuation of Exercise Cinemax from Week4Day2 XP”
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Given the following object:
# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

# ---------------------------------------------------------------

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total = 0
# for key, value in family.items():
#     if value > 12:
#         indi_ticket = 15
#         total += 15
#         print(f"{key} your age is {value} and your ticket costs ${indi_ticket}.")
#     elif 3 < value <= 12:
#         indi_ticket = 10
#         total += 10
#         print(f"{key} your age is {value} and your ticket costs ${indi_ticket}.")
#     elif value <= 3:
#         indi_ticket =  0
#         total +=0
#         print(f"{key} your age is {value} and your ticket costs ${indi_ticket}.")
# print(f"Your new total is {total}")

# ---------------------------------------------------------------
# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# ---------------------------------------------------------------
# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona" ,
#     "type_of_clothes": {
#         "men", 
#         "women", 
#         "children", 
#         "home",
#         },
#     "international_competitors": {
#         "Gap",
#         "H&M", 
#         "Benetton"
#         }, 
#     "number_stores": 7000,
#     "major_color":{ 
#         "France": "blue", 
#         "Spain": "red", 
#         "US":" pink, green"
#         }
# }
# brand["number_stores"] = 2 # 3. Change the number of stores to 2.
# brand["Clients"] = "These are who our clients are..." # 4. Print a sentence that explains who Zaras clients are.
# brand["Country creation"] = "spain" # 5. Add a key called country_creation with a value of Spain.
# brand["international_competitors"] = "Gap", "H&M", "Benetton", "desigual" # 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# del brand["creation_date"] # 7. Delete the information about the date of creation.
# print(brand["international_competitors"][3])# 8. Print the last international competitor.
# print(brand["major_color"]["US"])# 9. Print the major clothes colors in the US.
# for index, keys in enumerate(brand.items()):# 10. Print the amount of key value pairs (ie. length of the dictionary).
#     print(index, keys)
# for keys in brand:
#     print(keys)    # 11. Print the keys of the dictionary.   

# # 12. Create another dictionary called more_on_zara with the following details:
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
# }
# brand.update(more_on_zara)
# print(brand)   # 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# print(brand["number_stores"])  #recieve the last updated store total  # 14. Print the value of the key number_stores. What just happened ?
# ---------------------------------------------------------------
# Exercise 4 : Disney Characters
# Instructions
# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

# ---------------------------------------------------------------

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# nums = range(0, 6)
#1
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# for user in zip(users, nums):
#     print(user)
# print({v: k for k, v in enumerate(users)})
#2/
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# for user in zip(nums, users):
#     print(user)
# for name in enumerate(users):
#     print(name)

#3/ 
# # >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
sorted = sorted(users)
# for user in zip(sorted, nums):
#     print(user)
print({v: k for k, v in enumerate(sorted)})
