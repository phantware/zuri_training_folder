'''
In Python, a function is a group of related statements that performs a specific task
Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable
 
Creating functions
Python uses def  keyword to start a function, here is the syntax:

def function_name(arg1, arg2, arg3, .... argN):
     #statement inside function

 Note: All the statements inside the function should be indented using equal spaces. Function can accept zero or more arguments(also known as parameters) enclosed in parentheses. You can also omit the body of the function using the pass keyword, like this:

def myfunc():
    pass
'''
def nameOfFunction():
    print("This is a function")

nameOfFunction()  # This is a function
nameOfFunction()  # This is a function
nameOfFunction()  # This is a function

def nameOfFunction(name, count):
    print("%s call function with count %d" (name, count))

nameOfFunction(4)  # Seyi call function with count 4

def nameOfFunction(count):
    print("This is a function %d" %count)

nameOfFunction(4)  # This is a function 4

def sum(start, end):
   result = 0
   for i in range(start, end + 1):
       result += i
   print(result)

sum(1, 10)

# Above we define a function called sum() with two parameters start and end. The function calculates the sum of all the numbers starting from start to end.

'''
Function with return value.

The above function simply prints the result to the console, what if we want to assign the result to a variable for further processing? Then we need to use the return statement. The return statement sends a result back to the caller and exits the function.
'''
def sum(start, end):
   result = 0
   for i in range(start, end + 1):
       result += i
   return result

s = sum(1, 10)
print(s)

'''
Here we are using the return statement to return the sum of numbers and assign it to variable s.

You can also use the return statement without a return value.
'''
def sum(start, end):
   if(start > end):
       print("start should be less than end")
       return    # here we are not returning any value so a special value None is returned
   result = 0
   for i in range(start, end + 1):
       result += i
   return result

s = sum(110, 50)
print(s)

'''
Global variables vs local variables
Global variables: Variables that are not bound to any function , but can be accessed inside as well as outside the function are called global variables.

Local variables: Variables which are declared inside a function are called local variables.

Let's see some examples to illustrate this point.

Example 1:

'''
global_var = 12         # a global variable
def func():
    local_var = 100     # this is local variable
    print(global_var)   # you can access global variables in side function

func()                  # calling function func()

#print(local_var) 

# You can bind local variable in the global scope by using the global keyword followed by the names of variables separated by comma (,).

t = 1

def increment():
    global t   # now t inside the function is same as t outside the function
    t = t + 1
    print(t) # Displays 2


increment()
print(t) # Displays 2

# Argument with default values
# To specify default values of argument, you just need to assign a value using assignment operator.

def func(i, j = 100):
    print(i, j)

func(2)
# Above function has two parameter i and j. The parameter j has a default value of 100, it means that we can omit value of j while calling the function.

'''
Keyword arguments #
There are two ways to pass arguments to method: positional arguments and Keyword arguments. We have already seen how positional arguments work in the previous section. In this section we will learn about keyword arguments.

Keyword arguments allows you to pass each arguments using name value pairs like this name=value. Let's take an example:
'''
def named_args(name, greeting):
    print(greeting + " " + name )
named_args(name='jim', greeting='Hello')
named_args(greeting='Hello', name='jim') # you can pass arguments this way too

# Mixing Positional and Keyword Arguments #
# It is possible to mix positional arguments and Keyword arguments, but for this positional argument must appear before any Keyword arguments. Let's see this through an example.

def my_func(a, b, c):
    print(a, b, c)

# You can call the above function in the following ways.

# using positional arguments only
my_func(12, 13, 14)     

# here first argument is passed as positional arguments while other two as keyword argument
my_func(12, b=13, c=14) 

# same as above
my_func(12, c=13, b=14) 

# this is wrong as positional argument must appear before any keyword argument 
# my_func(12, b=13, 14)

# Returning multiple values from Function
# We can return multiple values from function using the return statement by separating them with a comma (,). Multiple values are returned as tuples.

def bigger(a, b):
    if a > b:
        return a, b
    else:
        return b, a

s = bigger(12, 100)
print(s) #  (100, 12)
print(type(s))  #  <class 'tuple'>


