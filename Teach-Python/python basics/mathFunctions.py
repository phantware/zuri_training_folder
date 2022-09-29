"""
Python has many inbuilt function.

Method	                     Description
round(number[, ndigits])	   rounds the number, you can also specify precision in the second argument
pow(a, b)	                  Returns a raise to the power of b
abs(x)	                     Return absolute value of x
max(x1, x2, ..., xn)	       Returns largest value among supplied arguments
min(x1, x2, ..., xn)	       Returns smallest value among supplied arguments
"""
# Below mentioned functions are in math module, so you need to import math module first, using the following line.

# Let's take some examples to understand better

abs(-22)               # Returns the absolute value  result = 22

max(9, 3, 12, 81)      # Returns the maximum number result = 81

min(78, 99, 12, 32)    # Returns the minimum number result = 12

pow(8, 2)              # can also be written as 8 ** 2 result = 64

pow(4.1, 3.2)          # can also be written as 4.1 ** 3.2 result = 91.39203368671122

round(5.32)            # Rounds to its nearest integer result = 5

round(3.1456875712, 3) # Return number with 3 digits after decimal point result = 3.146


"""
Method	       Description
ceil(x)	      This function rounds the number up and returns its nearest integer
floor(x)	     This function rounds the down up and returns its nearest integer
sqrt(x)	      Returns the square root of the number
sin(x)	       Returns sin of x where x is in radian
cos(x)	       Returns cosine of x where x is in radian
tan(x)	       Returns tangent of x where x is in radian

"""
import math

math.ceil(3.4123)  # result = 4

math.floor(24.99231) # result = 24