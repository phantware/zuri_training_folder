# register
# username, password, email
# generate user account

# login
# (username or email) and password

# Bank operation

# Initialize the system

database = {}
def init():
 
 isValidOption = False;
 
 print("Welcome to Access Bank ")
 print()
 
 while isValidOption == False:
   haveAccount = int(input("Do you have an account with us? Enter 1 to login or 2 to register: "))
   if(haveAccount == 1):
    isValidOption = TRUE
    login()
     
   elif(haveAccount == 2):
    isValidOption = TRUE
    register()
   else:
    print("You have selected an invalid option, please try again")
    print()


def login():
 print("This is the login function ")

def register():
 print("This is the register function ")

def bankOperations():
 print("Some operations ")
 
def generateAccountNumber():
 print("Account number generator ")


### ACTUAL BANKING SYSTEM ###

init()