# Find the sum of all the primes below two million.
def func():
    sum = 0
    for i in range(2, 2000000):
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            sum += i
    print(sum)

if __name__ == '__main__':
    func()
