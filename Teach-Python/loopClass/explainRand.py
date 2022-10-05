# import random

# rand_num = random.randrange(1,51)

# i = 1

# while(i != rand_num):
#  i += 1
    
# print("The random value is : ", rand_num)

# Using continue and break

i = 1

while i <= 20:
  if (i % 2) == 0:
     i += 1
     continue
 
  if i == 15:
     break
  print("Odd : ", i)
  i += 1