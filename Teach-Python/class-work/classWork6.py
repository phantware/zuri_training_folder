# Passwor checker
# Write a program that ask the users to input their username and password
# Encrypt the password
# Print the user name and their password length

# Solution

username = input("Enter your username: ")
password = input("Enter your password: ")
passwordLength = len(password)
hiddenPassword = '*' * passwordLength

print(f"Welcome {username}, your password is {hiddenPassword}, and it's {passwordLength} letter long")


