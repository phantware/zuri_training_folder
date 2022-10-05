# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment + their investment * interest rate 
# Print out the earnings after a 10 year period

# HINT: 
# Ask for the money invested + the interest rate
# Convert the value to a float
# Convert the value to a float and round the percentage rate by 2 digits
# Cycle through 10 years using a for loop and range from 0 to 9
# Output the results

# Solution

money =  input("How much to invest: ")
interest_rate = input("Interest Rate: ")
money = float(money)
interest_rate = float(interest_rate) * .01

for i in range(10):
  money = money + (money * interest_rate)

print("Investment after 10 years : {:.2f}".format(money))