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

# Iterating string using for loop
# String is a sequence type and also iterable using for loop (to learn more about for loop click here ).

s = "hello"
for i in s:
  print(i, end="") # hello

"""
Testing strings
String class in python has various inbuilt methods which allows to check for different types of strings.

Method name	       Method Description
isalnum()	         Returns True if string is alphanumeric
isalpha()	         Returns True if string contains only alphabets
isdigit()	         Returns True if string contains only digits
isidentifier()	    Return True is string is valid identifier
islower()	         Returns True if string is in lowercase
isupper()	         Returns True if string is in uppercase
isspace()	         Returns True if string contains only whitespace
"""
s = "welcome to python"
s.isalnum() # False

"Welcome".isalpha() # True

"2012".isdigit() # True

"first Number".isidentifier() # False

s.islower() # True

"WELCOME".isupper() # True

"  \t".isspace() # True

"""
Searching for Substrings

Method Name	                    Methods Description

endswith(s1: str): bool	        Returns True if strings ends with substring s1
startswith(s1: str): bool	      Returns True if strings starts with substring s1
count(substring): int	          Returns number of occurrences of substring the string
find(s1): int	                  Returns lowest index from where s1 starts in the string, if string not
                                found returns -1
rfind(s1): int	                 Returns highest index from where s1 starts in the string, if string not
                                found returns -1
"""

s = "welcome to python"
s.endswith("thon") # True

s.startswith("good") # False

s.find("come") # 3

s.find("become") # -1

s.rfind("o") # 15

s.count("o") # 3

"""
Converting Strings

Method name	           Method Description
capitalize(): str	     Returns a copy of this string with only the first character capitalized.
lower(): str	          Return string by converting every character to lowercase
upper(): str	          Return string by converting every character to uppercase
title(): str	          This function return string by capitalizing first letter of every word in the string
swapcase(): str	       Return a string in which the lowercase letter is converted to uppercase and
                       uppercase to lowercase
replace(old\, new):str	This function returns new string by replacing the occurrence of old string with new
                        string
"""

s = "string in python"

s1 = s.capitalize()
s1 # 'String in python'

s2 = s.title()
s2 # 'String In Python'

s = "This Is Test"
s3 = s.lower()
s3 # 'this is test'

s4 = s.upper()
s4 # 'THIS IS TEST'

s5 = s.swapcase()
s5 # 'tHIS iS tEST'

s6 = s.replace("Is", "Was")
s6 # 'This Was Test'
s # 'This Is Test'
