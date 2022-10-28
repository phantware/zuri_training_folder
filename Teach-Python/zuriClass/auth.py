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
 isLoginSuccessful = False
 
 while isLoginSuccessful == False:
  accountNumberFromUser = int(input("What is your account number? "))
  password = input("What is your password ")
  
  for accountNumber, userDetails in database.items():
   if(accountNumber == accountNumberFromUser):
    if(userDetails[3] == password):
     isLoginSuccessful = True;
  print("Invalid account or password")
 
 bankOperations(userDetails)

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
 print(" == === ==== ===== ==== === == ")
 print("Your account number is: %d" % accountNumber)
 print("Make sure you keep it safe")
 print(" == === ==== ===== ==== === == ")
 
 
 login() 
 
def bankOperations(user):
 print("Welcome %s %s " % (user[0], user[1]))
 
 selectedOption = int(input("What would you like to do? Select (1) for Deposite, (2) for Withdrawal, (3) for Logout, (4) for Exit"))
 
 if(selectedOption == 1):
  depositOperation()
 elif(selectedOption == 2):
  withdrawalOperation()
 elif(selectedOption == 3):
  login()
 elif(selectedOption == 4):
  exit()
 else:
  print("Invalid option selected")
  bankOperations(user)
 

def withdrawalOperation():
 print("Withdrawal Operation")
 
def depositOperation():
 print("Deposit Operation")
 
 
def generateAccountNumber():
 return random.randrange(1111111111,9999999999)
# print(generateAccountNumber())



### ACTUAL BANKING SYSTEM ###

init()