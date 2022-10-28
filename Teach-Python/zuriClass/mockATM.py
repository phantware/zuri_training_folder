name = input("What is your name? ")
allowedUsers = ["Seyi","Mike","Love"]
# allowedPassword = "Password"
allowedPassword = ["seyi12345", "mike12345","love01"]

# newUser = input("Please enter your name ")
# allowedUser.append(newUser)
# print('allowed user', allowedUsers)


if(name in allowedUsers):
 password = input("Your password? ")
 userId = allowedUsers.index(name)

 if(password == allowedPassword[userId]):
  print("Welcome " + name)
  
  print("These are the available options: ")
  print("1. Withdrawal")
  print("2. Cash Deposit")
  print("3. Complaint")

  selectedOption = int(input("Please select an option "))
  
  if(selectedOption == 1):
   print("You selected %s" % selectedOption)
   print
  elif(selectedOption == 2):
   print("You selected %s" % selectedOption)
   print
  elif(selectedOption == 3):
   print("You selected %s" % selectedOption)
   print
  else:
   print("Invalid option selected, please try again")
  
 else:
  print("Password Incorrect, please try again")

else:
 print("Name not found, please try again")