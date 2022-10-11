"""
 Solve for x
 x + 4 = 9
 
 Hint:
 
 x will always be the 1st value received and you only will deal with addition
 Receive the string and split the string into variables
 Convert the string into ints
 Convert the result into a string and join it to the string "X = "
 print()
 
 Solution
"""
def solve_eq(equation):
 x, add, num1, equal, num2 = equation.split()
 num1, num2 = int(num1), int(num2)
 
 return "x = " + str(num2 - num1)

print(solve_eq("x + 4 = 9"))