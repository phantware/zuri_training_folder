import random

input("Welcome to Rock, Paper and Scissors! Press enter to start ")

user_score = 0
cpu_score = 0

while True:
 print()
 user_choice = input("Rock, Paper, or Scissors?: ").lower()

 while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
  user_choice = input("Invalid input, please try again: ").lower()

 random_num = random.randint(0,2)
 if random_num == 0:
  cpu_choice = "rock"
 elif random_num == 1:
  cpu_choice = "paper"
 elif random_num == 2:
  cpu_choice = "scissors"

 print()
 print("Your choice: ", user_choice)
 print("Computer's choice: ", cpu_choice)
 print()

 if user_choice == "rock":
  if cpu_choice == "rock":
   print("It's a tie!")
  elif cpu_choice == "paper":
   print("You lost!")
   cpu_score += 1
  elif cpu_choice == "scissors":
   print("You win!")
   user_score += 1
   
 elif user_choice == "paper":
  if cpu_choice == "paper":
   print("It's a tie!")
  elif cpu_choice == "scissors":
   print("You lost!")
   cpu_score += 1
  elif cpu_choice == "rock":
   print("You win!")
   user_score += 1

 elif user_choice == "scissors":
  if cpu_choice == "scissors":
   print("It's a tie!")
  elif cpu_choice == "rock":
   print("You lost!")
   cpu_score += 1
  elif cpu_choice == "paper":
   print("You win!")
   user_score += 1
 
 print()
 print("You have", user_score, "wins")
 print("The Computer has", cpu_score, "wins")
 print()

 repeat = input("Play again? (Y/N) ").lower()
 while repeat != "n" and repeat !="y":
  repeat = input("Invalid input, please try again: ").lower()

 if repeat == "n":
  break
 print("\n----------------------------------------------------\n")
