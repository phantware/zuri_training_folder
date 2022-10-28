name = input("What is your name? ")
allowedUser = ["Seyi","Mike","Love"]
allowedPassword = "Password"

if(name in allowedUser):
 password = input("Your password? ")

 if(password == allowedPassword):
  print("Welcome " + name)
 else:
  print("Password Incorrect, please try again")

else:
 print("Name not found, please try again")