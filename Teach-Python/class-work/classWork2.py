# Problem: Receive miles and convert to kilometers
# Kilometers = miles * 1.60934
# Enter Miles 5
# 5 Miles equals 8.04 kilometers

## Solution
# Ask the users to input miles and assign it to miles variable
miles  =  input( 'Enter Miles ')
# Convert from string to integer
miles = int(miles)
# Perform calculation by multiplying 1.60934 times miles save in variable called kilometers
kilometers = miles * 1.60934
#Print result using format()
print("{} miles equals {} kilometers".format(miles, kilometers))