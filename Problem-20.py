# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 01:15:06 2022

@author: Saadettin
"""
fact = 1
for i in range(100,0,-1):
    fact *= i

fact = str(fact)

sum = 0

for i in range(0,len(fact)):
    sum += int(fact[i])
print(sum)