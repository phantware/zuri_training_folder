# Set is an  unordered collection of a unique object
# In set, we don't have key value pairs
# In a set, there is no duplicate, everything has to be unique

from multiprocessing.reduction import duplicate


my_set = {1,2,3,4,5}
print(my_set)  # result = {1,2,3,4,5}

my_set = {1,2,3,4,5,5}
print(my_set)  # result = {1,2,3,4,5}

# to turn a list into a set and remove duplicate, see below code
my_list = [1,2,3,4,5,5,6,7]
print(set(my_list)) # result = {1,2,3,4,5,6,7}

