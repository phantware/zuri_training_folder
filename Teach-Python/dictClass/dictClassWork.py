
# Using your knowledge of how dictionary works, create a program to get an employees information from the user input
# Print out the result in a dictionary format

employees = []
fName, lName = input("Enter Employee Name: ").split()
employees.append({"fName":fName, "lName": lName})
print(employees)