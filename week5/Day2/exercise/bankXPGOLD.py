
# TODO: Exercise 1: Bank Account
# Instructions
# Part I:
# Create a class called BankAccount that contains the following attributes 
# and methods:
# balance - (an attribute)
# __init__ : initialize the attribute
# deposit : - (a method) accepts a positive int and adds to the balance, 
# raise an Exception if the int is not positive.
# withdraw : - (a method) accepts a positive int and deducts 
# from the balance, raise an Exception if not positive
# ------------------------------------------------------------
# TODO Part II : Minimum balance account

# Create a MinimumBalanceAccount that inherits from BankAccount.
# Extend the __init__ method and accept a parameter called minimum_balance 
# with a default value of 0.
# Override the withdraw method so it only allows the user to withdraw money 
# if the balance remains higher than the minimum_balance, raise an Exception if not.
# ------------------------------------------------------------
# TODO : Part III: Expand the bank account class

# Add the following attributes to the BankAccount class:
# username
# password
# authenticated (False by default)

# Create a method called authenticate. This method should accept 2 strings :
# a username and a password. If the username and password match the attributes username and
#  password the method should set the authenticated boolean to True.

# Edit withdraw and deposit to only work if authenticated is set to True, 
# if someone tries an action without being authenticated raise an Exception
# ------------------------------------------------------------
class BankAccount():
    def __init__(self, username, password, balence = 0, athenticated = False):
        self.username = username
        self.password = password
        self.balence = balence
        self.athenticated = athenticated
        self.transaction = []

    def athenticate(self):
        username = input("Please enter a username: ")
        if username == self.username:
            password = input("Please enter your password: ")
            if password == self.password:
                self.athenticated = True
        else: 
            raise Exception("Either your Username or Password is incorrect.")

    def deposit(self):
        if self.athenticated == True:
            amount = int(input("how much would you like to deposit: "))
            if amount <= 0:
                raise Exception("You entered a negative deposit. Please re-enter a correct positive deposit")
            else:
                self.balence += amount
                self.transaction.append(amount)
                print(f"{self.username}'s deposit has been approved")
        else: 
            raise Exception("You need to authenticate yourself before the ability to make a deposit.")

    def withdraw(self):
        if self.athenticated == True:
            amount = int(input("how much would you like to withdraw: "))
            if amount >= self.balence:
                raise Exception("Insufficiant funds.")
            else:
                self.balence -= amount
                self.transaction.append(amount)
                print(f"{self.username}'s withdraw has been approved")
        else:
            raise Exception("You need to authenticate yourself before the ability to make a withdrawel.")

    def transaction(self):
        if self.athenticated == True:
            print("TRANSACTIONS")
            print("------------")
            for transaction in self.transaction:
                print(f"{self.username}'s history of transactions: {transaction}. Amount total: {self.balence}")
        else:
            raise Exception("This information is private. You have yet to athenticate yourself.")

class MinimumBalanceAccount(BankAccount):
    def __init__(self, name, min_balance=0):
        self.min_balence = min_balance
        super().__init__(name, balence = 0)
    
    def withdraw(self, amount):
        if (self.balence - amount) >= self.min_balence:
            self.balence -= amount
            self.transaction.append(self.balence)
            print(f"{self.name}, your withdraw request of: {amount}, has been Approved")
            print(f"{self.name}, your new total is: {self.balence}")
        else:
            raise Exception(f"This request takes your min balence below {self.min_balence}. Your request has been denied.")
# ------------------------------------------------------------
# todo: Part IV: BONUS Create an ATM class
# __init__:
# Accepts the following parameters: account_list and try_limit.
# Validates that account_list contains a list of BankAccount 
# or MinimumBalanceAccount instances.
# Hint: isinstance()

# Validates that try_limit is a positive number, 
# if you get an invalid input raise an Exception, then move along 
# and set try_limit to 2.
# Hint: Check out this tutorial

# Sets attribute current_tries = 0

# ------------------------------------------------------------
# class ATM(BankAccount):
#     def __init__(self, try_limit = 3):
#         self.try_limit = try_limit
#         self.account_list = []
#         super().__init__(BankAccount.username, BankAccount.password, balence = 0, athenticated = False)


        # current_tries = 0
        # self.account_list.append(BankAccount.username)
        # for account in self.account_list:
        #     if isinstance(account, BankAccount):
        #         self.account_list.append(account)
        #     elif isinstance(account, MinimumBalanceAccount):
        #         self.account_list.append(account)
        # for account in self.account_list:
        #     try:
        #         BankAccount.athenticate()
        #         break
        #     except:
        #         current_tries +=1
        #         remainder = self.try_limit - current_tries
        #         print(f"You have {remainder} attempts remaining.")
        #         break
        #     finally:
        #         if current_tries < self.try_limit:
        #             print("You have reached maximum attempts for this account.")

my_account = BankAccount("gerki", "12345", 10)
# atm_account = ATM()
# ATM.add_to_atm(my_account)
my_account.athenticate()
# print(my_account.athenticated)
my_account.deposit()
# my_other_account = BankAccount("gerki")
# BankAccount.deposit(my_other_account, 550)
print(my_account.transaction)
BankAccount.withdraw(my_account)
BankAccount.transaction(my_account)

# my_account1 = MinimumBalanceAccount("j")
# my_account1.deposit(500)
# print(my_account1.transaction)
# my_account1.withdraw(455)
    
# ------------------------------------------------------------
# Call the method show_main_menu (see below)
# Methods:
# show_main_menu:
# This method will start a while loop to display a menu letting a user select:
# Log in : Will ask for the users username and password 
# and call the log_in method with the username and password (see below).
# Exit.

# log_in:
# Accepts a username and a password.

# Checks the username and the password against all accounts in account_list.
# If there is a match (ie. use the authenticate method), call the method show_account_menu.
# If there is no match with any existing accounts, increment the current tries by 1. 
# Continue asking the user for a username and a password, until the limit is reached (ie. try_limit attribute). 
# Once reached display a message saying they reached max tries and shutdown the program.

# show_account_menu:
# Accepts an instance of BankAccount or MinimumBalanceAccount.
# The method will start a loop giving the user the option to deposit, withdraw or exit.
# ------------------------------------------------------------

