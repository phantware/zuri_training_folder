# defining a function in python
num_3 = "3.142"

def isFloat(str_val):
 try:
  float(str_val)
  return True
 except ValueError:
  return False
print("Is PI a Float? ", isFloat(num_3))

