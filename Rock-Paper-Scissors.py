import random

user_choice = input("Rock, Paper, or Scissors: ")

random_num = random.randint(0,2)
if random_num == 0:
 cpu_choice = "rock"
elif random_num == 1:
 cpu_choice = "paper"
elif random_num == 2:
 cpu_choice = "scissors"

print()
print("Your choice:", user_choice)
print("Computer's choice:", cpu_choice)