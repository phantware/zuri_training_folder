# Creating module
# Create a new file called mymodule.py and write the following code.

# foo = 100

# def hello():
#     print("i am from mymodule.py")

# As you can see we have defined a global variable foo and a function hello() in our module. Now to use this module in our programs we first need to import it using import statement like this

import mymodule
# Now you can use variable and call functions in the mymodule.py using the following code.

import mymodule

print(mymodule.foo)
print(mymodule.hello())

'''
Expected Output:

100
i am from mymodule.py

Remember you need to specify name of module first to access it's variables and functions, failure to so will result in error.
'''

'''
Using from with import
Using import statements imports everything in the module, what if you want to access only specific function or variable? This is where the from statement comes, here is how to use it.
'''

from mymodule import foo # this statement import only foo variable from mymodule
print(foo)

# Expected output: result = 100

'''
dir() method
The dir() is an in-built method used to find all attributes (i.e all available classes, functions, variables and constants ) of the object. As we have already discussed everything in python is object, we can use the dir() method to find attributes of the module like this:

dir(module_name)
The dir() returns a list of string containing the names of the available attributes.
'''

dir(mymodule)
['__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__', 'foo', 'hello']

# As you can see besides foo and hello there are additional attributes in the mymodule. These are in-built attributes which python provides to all the modules automatically.
