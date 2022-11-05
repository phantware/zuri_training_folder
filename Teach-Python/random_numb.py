import random
# create a random word using the random function
words = ['home', "game", 'toy', 'smart', 'able', 'hold']
choices = random.choice(words)
#create an empty list and a filled list to hold the values created
empty_list = []
filled_list = []
# print a message to the user telling them the random word to be completed
print(f"The random word is {choices}")
#create  two lists that holds a '_' in place of the each word and the one that holds the complete respectively

for choice in choices:
  empty_list.append('_')

for choice in choices:
  filled_list.append(choice)
print(empty_list)

# ask the user to enter any word that is contained the random string supplied by the interpreter


def valueCheck():
  #
  while True:
    user_letter = input("Enter a letter: ").lower()
    # loop through the (random) word given and check if user input matches any letter in that word
    if user_letter not in filled_list:
      print("\t Incorrect letter")

    else:
      #get index of the letter provided from the filled list
      index = filled_list.index(user_letter)
      #place the letter provided at the index found
      empty_list[index] = user_letter
      print(empty_list)

      if '_' in empty_list:
        valueCheck()
      # once the list is complete, end the program .
      break


valueCheck()