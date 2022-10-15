# Write a program to return a list of prime numbers
# A prime can only be divid by 1 and itself

# Input maximum prime to search for
# Use a for loop to check if modulus == 0

# Solution

def is_prime(num):
 for i in range(2,num):
  if(num % i) == 0:
   return False
 return True

def getPrime(max_number):
 list_of_primes = []
 
 for num1 in range(2, max_number):
  if is_prime(num1):
   list_of_primes.append(num1)

 return list_of_primes

max_num_to_check = int(input("Search for prime up to: "))

list_of_primes = getPrime(max_num_to_check)

for prime in list_of_primes:
 print(prime)
  