# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

#999*999 ,999 * 998, 998*998, 998* 997

def func():
    i = 999
    j = 999
    counter = 0

    while True:
        if i == 500 or j == 500:
            break
        palindromic = i * j
        firstDigit  = palindromic / 100000
        firstDigit  = int(firstDigit)
        lastDigit   = palindromic % 10
        if firstDigit == lastDigit:
            secondDigit = palindromic / 10000
            secondDigit = int(secondDigit)
            secondDigit = secondDigit % 10
            last2Digit  = palindromic % 100
            last2Digit  = (last2Digit - lastDigit) / 10
            last2Digit = int(last2Digit) 
            if secondDigit == last2Digit:
                thirdDigit = palindromic / 1000
                thirdDigit = int(thirdDigit)
                thirdDigit = thirdDigit % 10
                last3Digit = palindromic % 1000
                last3Digit = (last3Digit - last2Digit - lastDigit) / 100 
                last3Digit = int(last3Digit)
                if thirdDigit == last3Digit:
                    print(i,j)
        counter += 1
        if counter % 3 == 0:
            i -= 1
        else:
            j -= 2
         
if __name__ == '__main__':
    func()