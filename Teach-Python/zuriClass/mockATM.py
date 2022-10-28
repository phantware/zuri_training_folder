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
 else:
  print("Password Incorrect, please try again")

else:
 print("Name not found, please try again")