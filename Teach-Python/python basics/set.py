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


# Set Methods

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9.10}

result = my_set.difference(your_set)
print(result) # result = {1,2,3} it found the difference btw the two sets

print(my_set.discard(5)) # This remove 5 from the list
print(my_set) # result = {1,2,3,4 }

result2 = my_set.difference_update(your_set)  # This removes all elements of another set from this set
print(result2)  # None
print(my_set) # result = {1,2,3} 4 and 5 which is the difference are removed

result3 = my_set.intersection(your_set)  # This interset the common things in the set
print(result3)  # {4,5}

result4 = my_set.isdisjoint(your_set)  # This returns true if two sets have a null intersection (They have nothing in common) print(my_set & your_set)
print(result4)  # False

result4 = my_set.union(your_set)  # This returns the union of sets as a new set
print(result4)  # {1,2,3,4,5,6,7,8,9,10} it unites all the sets and remove duplicate print(my_set | your_set)

result5 = my_set.issubset(your_set) # This reports whether another set contains this set
print(result5) # Returns True if it contains  --> (if my_set is inside of your_set)

result6 = your_set.issuperset(my_set) # Reports whether this set contains another set
print(result6) # Returns True if it does not contains