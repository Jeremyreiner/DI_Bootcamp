# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#      ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~
#    The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !
# ------------------------------------------------------------------------------

age = input("Please enter your birthday in the format (DD/MM/YYYY): ").replace("/", " ")
list_age = age.split()
# print(list_age)
years = int(list_age[-1])
current_age = 2021 - years
last_digit = str(current_age)[1:]
print(last_digit)
# Add candles to cake
candles = "___" +("i" * int(last_digit)) +"___" 
cake =f'''
      {candles}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
'''
print(cake)

# Find if the year is a leap year
if years % 4 == 0:
    print(cake)