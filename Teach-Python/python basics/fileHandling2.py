# Reading and Writing text to a file
# Importing os module, this helps us to manipulate files
# The greatest thing about being able to reading and write file is that we will be able for later use
# We can as well read an already created file with a function called open. 
# When we use with, this guarantee the file will be closed if the program should crash
# Whenever we define that we want to use utf-8, what that is saying is that we want to store our text using Unicode
# read(), this is going to reads everything into one string up to it gets to a new line 
# readline(), this is going to read everything including all new lines and with a string
# readlines(). this is going to return a list of everyline which is also going include all of your new lines.

import os
with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some randome text\nMore randome text\nAnd some new line")

with open("mydata.txt", encoding="utf-8") as myFile:
   print(myFile.read())

print(myFile.closed) # True
print(myFile.name) # mydata.txt
print(myFile.mode) # r

os.rename("mydata.txt", "mydata2.txt")  # This rename mydata.txt to mydata2.txt
os.remove("mydata.txt")  # This removes the file
os.mkdir("mydir")  # This is used to create a directiry
os.chdir("mydir")  # This is used to change into the new directiry
print("Current Directory", os.getcwd()) # this prints the path to the new directory
os.chdir("..") # Moves backward
os.rmdir("mydir") # This removes the direcory

