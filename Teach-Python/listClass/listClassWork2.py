# 1. An outer loop decreases in size each time 
# 2. The goal is to have the largest number at the end of the list when the outer loop completes 1 cycle]
# 3. The inner loop starts comparing indexes at the beginning
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at the end of the list 
# 7. Decrease the outer loop by 1

# Solution

import random
import math
numList = []
for i in range(5):
 numList.append(random.randrange(1,10))
 
i = len(numList) - 1
 
while i > 1:
 
 j = 0
 
 while j < i:
 
        # Tracks the comparison of index values
  print("\nIs {} > {}".format(numList[j], numList[j+1]))
  print()
 
        # If the value on the left is bigger switch values
if numList[j] > numList[j+1]:
 
 print("Switch")
 
 temp = numList[j]
 numList[j] = numList[j + 1]
 numList[j + 1] = temp
 
else:
 print("Don't Switch")
 
 j += 1
 
        # Track changes to the list
 for k in numList:
  print(k, end=", ")
  print()
 
 print("END OF ROUND")
