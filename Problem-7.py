# What is the 10 001st prime number?

def func():
    counter = 0
    for i in range(2, 9999999):
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            counter += 1
        if counter == 10001:
            print(i)
            break

if __name__ == '__main__':
    func()