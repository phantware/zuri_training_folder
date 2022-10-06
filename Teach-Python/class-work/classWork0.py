# Write a program that ask the users to input their birth year
# Remove the birth year from the current year
# Print you their real age

# Solution

birth_year = input("What year were you born: ")
age = 2022 - int(birth_year)

print(f"You are {age} years old")
