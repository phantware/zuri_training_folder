# But before we learn control statement, we need to learn about relational operators. Relational operators allows us to compare two objects.

'''
Symbol	      Description
<=	            smaller than or equal to
< 	            smaller than
> 	            greater than
>= 	         greater than or equal to
== 	         equal to
!= 	         not equal to

The result of comparision will always be a boolean value i.e True or False. Remember that, True and False are python keyword for denoting boolean values
'''

3 == 4  # False

12 > 3  #  True

12 == 12  #  True

44 != 12  #  True

'''
Now you are ready to tackle the if statements. The syntax of the if statement looks like this:

if boolean-expression:
   #statements
else:
   #statements

Note: Each statements in the if block must be indented using the same number of spaces, otherwise it will lead to syntax error. This is very different from languages like Java, C, C# where curly braces ({}) is used.

Now let's see an example
'''

i = 10

if i % 2 == 0:
   print("Number is even")
else:
   print("Number is odd")

# Here you can see that if number is even then "Number is even" is printed. otherwise "Number is odd" is printed.

# Note:
# The else clause is optional you can use only the if clause if you want, like this:

today = "party"
if today == "party":
    print("thumbs up!")

'''
Here, if the value of today is "party" then thumbs up! will get printed, otherwise nothing will print.

If your programs needs to check long list of conditions then you need to use if-elif-else statements.

if boolean-expression:
   #statements
elif boolean-expression:
   #statements
elif boolean-expression:
   #statements
elif boolean-expression:
   #statements
else:
   #statements
You can add as many elif condition as the programs demands.

Here is an example to illustrate if-elif-else statement.
'''
today = "monday"

if today == "monday":
   print("this is monday")
elif today == "tuesday":
   print("this is tuesday")
elif today == "wednesday":
   print("this is wednesday")
elif today == "thursday":
   print("this is thursday")
elif today == "friday":
   print("this is friday")
elif today == "saturday":
   print("this is saturday")
elif today == "sunday":
   print("this is sunday")
else:
   print("something else")

# Nested if statements #
# You can nest if statements inside another if statements as follows:

today = "holiday"
bank_balance = 25000
if today == "holiday":
   if bank_balance > 20000:
      print("Go for shopping")
   else:
      print("Watch TV")
else:
   print("normal working day")