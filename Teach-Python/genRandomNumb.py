# Python random module contains function to generate random numbers. So first you need to import random module using the following line.

import random

# random() Function #
# The random() function returns random number r such that 0 <= r < 1.0.

import random
for i in range(0, 10):
     print(random.random())

"""
Expected Output:

0.9240468209780505
0.14200320177446257
0.8647635207997064
0.23926674191769448
0.4436673317102027
0.09211695432442013
0.2512541244937194
0.7279402864974873
0.3864708801092763
0.08450122561765672
"""

# The randint(a, b) generate random numbers between a and b (inclusively).

import random
for i in range(0, 10):
   print(random.randint(1, 10))

# Expected Result: 8 3 4 7 1 5 3 7 3 3