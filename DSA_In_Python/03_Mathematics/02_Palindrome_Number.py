def palindromeNumber(num):
    temp, revNum = num, 0
    while temp > 0:
        revNum *= 10
        revNum = revNum + (temp % 10)
        temp //= 10
    return num == revNum

print(palindromeNumber(101))