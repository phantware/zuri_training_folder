# How do we deal in a situation where we have an unknown number of arguments been passed in our functions
# We receive an unknown number of arguments using splat operator

# Solution

def sumAll(*args):
  sum = 0
  
  for i in args:
    sum += i
  
  return sum

print("Sum :",sumAll(1,2,3,4,5))