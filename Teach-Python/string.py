name = "tom" # a string
mychar = 'a' # a character

name1 = str() # this will create empty string object
name2 = str("newstring") # string object containing 'newstring'

# Operations on string #
# String index starts from 0, so to access the first character in the string type:

name[0] # t

# The + operator is used to concatenate string and * operator is a repetition operator for string.

s = "tom and " + "jerry"
print(s) # tom and jerry

s = "spamming is bad " * 3
print(s) # 'spamming is bad spamming is bad spamming is bad '


'''
Slicing string #
You can take subset of string from original string by using [] operator also known as slicing operator.

Syntax: s[start:end]

This will return part of the string starting from index start to index end - 1.

Let's take some examples.
'''
s = "Welcome"
s[1:3] # el

"""
ord() and chr() Functions
ord() - function returns the ASCII code of the character.

chr() - function returns character represented by a ASCII number.
"""

ch = 'b'
ord(ch) # 98

chr(97) # 'a'

ord('A') # 65

"""
String Functions in Python
Function name	Function Description
len()	returns length of the string
max()	returns character having highest ASCII value
min()	returns character having lowest ASCII value
"""
len("hello") # 5

max("abc") # 'c'

min("abc") # 'a'

# in and not in operators
# You can use in and not in operators to check the existence of a string in another string. They are also known as membership operator.

s1 = "Welcome"
"come" in s1 # True

"come" not in s1 # False

"""
String comparison
You can use ( > , < , <= , <= , == , !=  ) to compare two strings. Python compares string lexicographically i.e using ASCII value of the characters.

Suppose you have str1 as "Mary"  and str2 as "Mac". The first two characters from str1  and str2 ( M and M ) are compared. As they are equal, the second two characters are compared. Because they are also equal, the third two characters (r and c ) are compared. And because r has greater ASCII value than c, str1 is greater than str2.

Here are some more examples:
"""
"tim" == "tie" # False

"free" != "freedom" # True

"arrow" > "aron" # True

"right" >= "left" # True

"teeth" < "tee" # False

"yellow" <= "fellow" # False

"abc" > "" # True
