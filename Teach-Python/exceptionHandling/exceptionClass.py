# To protect our code from braking, we use Error Handling to do that

while True:
 
   try:
    number = int(input("Please enter a number: "))
    break
   
   except ValueError:
    print("You don't enter a number")
    
print("Thank you for entering a number")
  