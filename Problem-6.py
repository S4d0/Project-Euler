# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

def func():
    sum      = 0
    squarSum = 0 
    for i in range(1, 101): # 101 wasn't count 
        sum      += i
        squarSum += i*i
    sum = sum*sum
    print(sum-squarSum)

if __name__ == '__main__':
    func()