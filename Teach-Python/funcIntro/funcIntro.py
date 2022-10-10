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


def change_name(name):
  return "Student" # name = "Student" To change the name, we return the name either

name = "Tola"

name = change_name(name) # change_name(name) We den reassign name to this

print(name)

# Global Variable: This works both inside and outside a function
gbl_name = "Sally"

def change_name2():
  global gbl_name
  gbl_name = "Lara"
  
change_name2()
print(gbl_name)




# defining a function in python
# num_3 = "3.142"

# def isFloat(str_val):
#  try:
#   float(str_val)
#   return True
#  except ValueError:
#   return False
# print("Is PI a Float? ", isFloat(num_3))

