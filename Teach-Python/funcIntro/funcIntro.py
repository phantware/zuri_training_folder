# Functions allow us to reuse code, we don't have to retype code over and over again

def add_number(num1, num2):
  return num1 + num2
print("5 + 4 = ", add_number(5,4))

# Local Variable: This only work inside a function
# Example:
def assing_name():
  name = "Lala"

assing_name()
print(name)   # This will through an error because name is a local variable

# Global Variable: This works both inside and outside a function


# defining a function in python
# num_3 = "3.142"

# def isFloat(str_val):
#  try:
#   float(str_val)
#   return True
#  except ValueError:
#   return False
# print("Is PI a Float? ", isFloat(num_3))

