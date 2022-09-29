# Creating a tuple #

t1 = () # creates an empty tuple with no data

t2 = (11,22,33)

t3 = tuple([1,2,3,4,4]) # tuple from array

t4 = tuple("abc") # tuple from string

# Tuples functions
# Functions like max(), min(), len() and sum() can also be used with tuples.

t1 = (1, 12, 55, 12, 81)
min(t1) #  1

max(t1) #  81

sum(t1)  #  161

len(t1)  #  5

# Iterating through tuples #
# Tuples are iterable using for loop [ Learn more about for loop here ] .

t = (11,22,33,44,55)
for i in t:
     print(i, end=" ")  #  11 22 33 44 55

# Slicing tuples
# Slicing operators works same in tuples as in list and string.

t = (11,22,33,44,55)
t[0:2]  #  (11,22)

# in and not in operator
# You can use in and not in operators to check existence of item in tuples as follows.

t = (11,22,33,44,55)
22 in t #  True

22 not in t #  False