# Creating a Dictionary #

# Dictionaries can be created using a pair of curly braces ({}). Each item in the dictionary consists of a key, followed by a colon, which is followed by a value. And each item is separated using commas (,). Let's take an example.

dictionary = {
'a': [1,2,3,4],
'b':'hello',
'c':True
}
print(dictionary)  #  {'a': [1,2,3,4], 'b': 'hello', 'c':True}
print(dictionary['a'])  #  [1,2,3,4]
print(dictionary['a'][1])  #  2

my_list = [
     {
'a': [1,2,3],
'b':'hello',
'c':True
},
{
'a': [4,5,6],
'b':'hello',
'c':True
}
]
print(my_list[0])  # This prints the firt Item
print(my_list[0]['a'][1])  # This prints 2


friends = {
'tom' : '111-222-333',
'jerry' : '666-33-111',
}

dict_emp = {} # this will create an empty dictionary

"""
Retrieving, modifying and adding elements in the dictionary
To get an item from the dictionary, use the following syntax:

dictionary_name['key']
"""

friends['tom'] # '111-222-333'

"""
To add or modify an item, use the following syntax:
dictionary_name['newkey'] = 'newvalue'
"""
friends['bob'] = '888-999-666'
friends #  {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}

"""
Deleting Items from the dictionary.
del dictionary_name['key']
"""
del friends['bob']
friends #  {'tom': '111-222-333', 'jerry': '666-33-111'}

# Looping items in the dictionary #
# You can use for loop to traverse elements in the dictionary.

friends = {
'tom' : '111-222-333',
'jerry' : '666-33-111'
}

for key in friends:
     print(key, ":", friends[key])

# tom : 111-222-333 
# jerry : 666-33-111

"""
Find the length of the dictionary
You can use the len() function to find the length of the dictionary.
"""
len(friends) # 2

# in or not in operators
# in and not in operators to check whether key exists in the dictionary.


'tom' in friends #  True

'tom' not in friends #  False

# Equality Tests in dictionary #
# The == and != operators tells whether dictionary contains the same items not.

d1 = {"mike":41, "bob":3}
d2 = {"bob":3, "mike":41}
d1 == d2 #  True

d1 != d2  #    False

# You can't use other relational operators like <, >, >=, <= to compare dictionaries.

"""
Dictionary methods
Python provides several built-in methods for working with dictionaries.

Methods	       Description
popitem()	       Returns randomly selected item from the dictionary and also remove the selected item.
clear()	       Delete everything from a dictionary
keys()	       Return keys in the dictionary as tuples
values()	       Return values in dictionary as tuples
get(key)	       Return value of key, if key is not found it returns None, instead of throwing KeyError
                 exception
pop(key)	       Remove the item from the dictionary, if the key is not found KeyError will be thrown
"""

friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}

friends.popitem() #  ('tom', '111-222-333')

friends.clear()
friends #  {}

friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}
friends.keys() #   dict_keys(['tom', 'bob', 'jerry'])

friends.values() #  dict_values(['111-222-333', '888-999-666', '666-33-111'])

friends.get('tom')  #   '111-222-333'

friends.get('mike', 'Not Exists')  #    'Not Exists'

friends.pop('bob')  #   '888-999-666'

friends  #  {'tom': '111-222-333', 'jerry': '666-33-111'}