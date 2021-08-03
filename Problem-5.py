# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

import math
p = 1
for i in range(1,21):
    p = math.lcm(p,i)
    print (p)