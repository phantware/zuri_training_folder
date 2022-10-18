
# Create a customer list
# Get information of the customer from the user input
'''
Hint:
Enter Customer (Yes/No): y
Enter Customer Name : Jamiu Ismail
Enter Customer (Yes/No): y
Enter Customer Name : Lara Ismail
Enter Customer (Yes/No): n
When the user enter n, it print out all the users inputs
Jamiu Ismail
Lara Ismail
'''
# Solution

# Create a list
customer = []
# Create a loop
while True:
 # Get input and make it work for y and n
 createEntry = input("Enter Customer (Yes/No) : ")
 createEntry = createEntry[0].lower()
 
 # Check to leave loop
 if createEntry == "n":
  break
 # Get customer data
 else:
  fName, lName = input("Enter Customer Name: ").split()
  
  # Add customer data to list
 customer.append({"fName": fName, "lName": lName})
# Print customer data
for cust in customer:
 print(cust)



