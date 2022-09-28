"""
Defining class
Class name in python is preceded with class keyword followed by a colon (:). Classes commonly contains data field to store the data and methods for defining behaviors. Also every class in python contains a special method called initializer (also commonly known as constructors), which get invoked automatically every time new object is created.

Let's see an example.
"""
class Person:

   # constructor or initializer
 def __init__(self, name): 
  self.name = name # name is data field also commonly known as instance variables

      # method which returns a string
  def whoami(self):
   return "You are " + self.name

# Here we have created a class called Person which contains one data field called name and method whoami().

"""
What is self?

All methods in python including some special methods like initializer have first parameter self. This parameter refers to the object which invokes the method. When you create new object the self parameter in the __init__  method is automatically set to reference the object you have just created.
"""

# Creating object from class

p1 = Person('tom') # now we have created a new person object p1
print(p1.whoami())
print(p1.name)

# Expected Output: You are tom tom

"""
Hiding data fields #
To hide data fields you need to define private data fields. In python you can create private data field using two leading underscores. You can also define a private method using two leading underscores.

Let's see an example
"""
class BankAccount:

     # constructor or initializer
    def __init__(self, name, money):
         self.__name = name
         self.__balance = money   # __balance is private now, so it is only accessible inside the class

    def deposit(self, money):
         self.__balance += money

    def withdraw(self, money):
         if self.__balance > money :
             self.__balance -= money
             return money
         else:
             return "Insufficient funds"

    def checkbalance(self):
         return self.__balance

b1 = BankAccount('tim', 400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.checkbalance())
print(b1.withdraw(800))
print(b1.checkbalance())

'''
Expected Output:

Insufficient funds
900
800
100
'''