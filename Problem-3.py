#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

num = 600851475143 
factors = []
curr = 2

while num > 1:
  if num % curr == 0:
    factors.append(curr)
    while num % curr == 0:
      num //= curr
  curr += 1

print(factors)