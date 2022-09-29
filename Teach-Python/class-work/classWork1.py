# Ask the user to input their name and assign it to a variable name called name
# Print out hello followed by the name the entered

# Solution

name = input("What is your name? ")
print("Hello ", name)


# Ask a user to input two values and store them in variable num1 and num2
# Solution

num1, num2 = input('Enter 2 numbers: ').split()

print(num1, num2)

# Convert the string into regular Integers
# Solution

num1 = int(num1)
num2 = int(num2)

# Add the value entered and store in sum
# Solution

sum = num1 + num2

# Subtract the value entered and store in difference
# Solution

difference = num1 - num2

# Multiply the value entered and store in product
# Solution

product = num1 * num2

# Divide the value entered and store in quotient
# Solution

quotient = num1 / num2

# Use modulus on the value to find the remainder
# Solution

remainder = num1 % num2

# Print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

