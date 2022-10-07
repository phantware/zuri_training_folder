# Guess a number between 1 and 10
# create a secret number
# Print out your guess is wrong if the user guess wrong
# Print you guess right

# Solution

secret_numb = 7

while True:
  guess = int(input("Guess a number between 1 and 10: "))

  if guess != secret_numb:
   print("You guess is wrong")
  else:
   print("You guess right")
   break