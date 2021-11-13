
import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Max1780'
DATABASE = 'MenuManager'
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()
from jsql_exerciseXP_day5_menuManager import MenuItem

# Create a file called menu_editor.py , which will have the following functions:
# load_manager()- this function should create a new MenuItem instance.
def load_manager(MenuItem):
    input_item = input("Chose a new item you would like to see on the menu: ")
    item_price = int(input("Enter a price for the new item: "))
    new_item = MenuItem(input_item, item_price)
    return MenuItem.save(new_item)
# show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to choose an item. 
# Call the appropriate function that matches the user’s input.
def show_user_menu(MenuItem):
    print("What would you like to order?\nA: Add an item\nB: Delete an item\nC: View the menu\nD: Exit")
    user_input = input().upper()
    while user_input != "D":
        if user_input == "A":
            # load_manager(MenuItem)
            break

        elif user_input == "B":
            # user_item = input("Enter an item you would like to delete: ")
            # price = int(input("Enter the price of the item: "))
            # item = MenuItem(f"{user_item}, {price}")
            print(MenuItem.delete(MenuItem))

        elif user_input == "C":
            return MenuItem.all(MenuItem)


menu_item = MenuItem(load_manager(MenuItem))

# add_item_to_menu() - this will ask the user to input the item’s name and price. 
# It will not interact with the menu itself, but simply call the appropriate function from the MenuItem object.
# If the item was added successfully print a message which states: item was added successfully.

# remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. 
# The function should not interact with the menu itself, but simply call the appropriate function from the MenuItem object.
# If the item was deleted successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.

# show_restaurant_menu() - print the restaurant’s menu.

# When the user chooses to exit the program, display the restaurant menu and exit the program.

# Here’s an example of the menu shown to the user: