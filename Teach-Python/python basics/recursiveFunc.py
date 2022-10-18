# Recursive function is a function that refers to itself, meaning it calls itself inside of itself
# Let say we want to calculate a factorials of 3! which is 3 * 2 * 1
# How will we use recussion to solve this problems?

def factorial(num):
 if num <= 1:
  return 1
 else:
  result = num * factorial(num - 1)
  return result
print("4! = ", factorial(4)) 

'''
DRY running the program

1st iteration: result  = 4 * factorial (4 - 1)  4 * 6
2st iteration: result  = 3 * factorial (3 - 1)  3 * 2 
3st iteration: result  = 2 * factorial (2 - 1)  2 * 1

'''