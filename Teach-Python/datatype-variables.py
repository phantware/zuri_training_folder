# Variables are named locations that are used to store references to the object stored in memory. The names we choose for variables and functions are commonly known as Identifiers. In Python, Identifiers must obey the following rules.

'''
All identifiers must start with a letter or underscore (_), you can't use digits. For e.g: my_var is a valid identifier but 1digit is not.
Identifiers can contain letters, digits and underscores (_). For e.g: error_404, _save are valid identifiers but $name$ ($ is not allowed) and #age (# is not allowed) are not.
They can be of any length.
Identifiers can't be a keyword. Keywords are reserved words that Python uses for special purposes). The following are keywords in Python 3.
'''

# In Python, you don't need to declare types of variables ahead of time. The interpreter automatically detects the type of the variable by the data it contains. To assign value to a variable equal sign (=) is used. The = sign is also known as the assignment operator.

'''
Python Data Types
Python has 5 standard data types namely.

1 - Numbers
2 - String
3 - List
4 - Tuple
5 - Dictionary
6 - Boolean - In Python, True and False are boolean literals. But the following values are also considered as false.
0 - zero , 0.0
[] - empty list , () - empty tuple , {} - empty dictionary ,  ''
None

'''

# x = 100                       # x is integer
# pi = 3.14                     # pi is float
# empname = "python is great"   # empname is string

# a = b = c = 100 # this statement assign 100 to c, b and a.

"""
Importing modules #
Python organizes codes using modules. Python comes with many built-in modules ready to use for e.g there is a math module for mathematical related functions, re module for regular expression, os module for operating system related functions and so on.

To use a module we first import it using the import statement. Its syntax is as follows:

import module_name

"""

import math, os

print(math.pi)
print(math.e)

print('current working dr', os.getcwd())