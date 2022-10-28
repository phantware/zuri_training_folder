# register
# first name, last name, password, email
# generate user account

# login
# (username or email) and password

# Bank operation

# Initialize the system

import random

database = {} # Dictionary
def init():
 
 isValidOption = False;
 
 print("Welcome to Access Bank ")
 print()
 
 while isValidOption == False:
   haveAccount = int(input("Do you have an account with us? Enter 1 to login or 2 to register: "))
   if(haveAccount == 1):
    isValidOption = True
    login()
     
   elif(haveAccount == 2):
    isValidOption = True
    print(register())
   else:
    print("You have selected an invalid option, please try again")
    print()


def login():
 print("Login to your account")
 print()
 
 bankOperations()

def register():
 print("Welcome to register page, kindly provide your details below")
 print()
 
 firstName = input("Please enter your First Name: ")
 lastName = input("Please enter your Last Name: ")
 email = input("Please enter your email: ")
 password = input("Please enter your password: ")
 accountNumber = generateAccountNumber()
 
 database[accountNumber] = [firstName, lastName, email, password]
 print()
 print("Your account has been successfully created")
 print()
 login() 
 
def bankOperations():
 print("Some operations ")
 
def generateAccountNumber():
 return random.randrange(1111111111,9999999999)
# print(generateAccountNumber())



### ACTUAL BANKING SYSTEM ###

init()