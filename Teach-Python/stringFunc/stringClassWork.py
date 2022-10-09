# Ask for a string and convert it to an acronyms
# Convert the string to uppercase
# Convert the string into a list
# Cycle through the list
# Get the 1st letter of the word and eliminate the new line
# Add a new line

# Solution

orig_string =  input("Conver to Acronym: ")
orig_string = orig_string.upper()
# print(orig_string)
list_of_words = orig_string.split()
# print(list_of_words)

for word in list_of_words:
 print(word[0], end="")

print()