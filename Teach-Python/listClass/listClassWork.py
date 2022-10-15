# Generate 5 values of a random list between 1 and 9

# Solution

import random
import math

numList = []
for i in range(5):
 numList.append(random.randrange(1,10))
 
for i in numList:
 print(i)