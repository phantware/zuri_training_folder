# Recursive function is a function that refers to itself, meaning it calls itself inside of itself
# Let say we want to calculate a factorials of 3! which is 3 * 2 * 1
# How will we use recussion to solve this problems?

# def factorial(num):
#  if num <= 1:
#    return 1
#  else:
#    result = num * factorial(num - 1)
#    return result
# print("4! = ", factorial(4)) 

'''
DRY running the program

1st iteration: result  = 4 * factorial (4 - 1)  4 * 6
2st iteration: result  = 3 * factorial (3 - 1)  3 * 2 
3st iteration: result  = 2 * factorial (2 - 1)  2 * 1

'''

# Calculate Fibonacci numbers
# For Fibonacci series, we have 1, 1, to calculate the next value we add the previous numbers together which = 2, it goes like that, 1, 1, 2, 3, 5, 8, 13
# To calculate this, we use the formula fn = fn - 1 + fn - 2
# Where F0 = 0, and F1 = 1
# print(fib(3))

'''
DRY running the program

1st iteration: result  = fib(2) + fib(1) :  2 + 1 = 3
2st iteration: result  = (fib(1) + fib(0 )) + fib(0) : 1 + 0  = 1
'''

def fibo(num):
 if num == 0:
   return 0
 elif num == 1:
  return 1
 else:
   result = fibo(num - 1) + (num - 2)
   return result
print(fibo(3))
print(fibo(4))
print(fibo(5))