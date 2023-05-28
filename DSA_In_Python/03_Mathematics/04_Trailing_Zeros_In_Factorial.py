def countTrailingZeros(num):
    count = 0
    while (num % 5 == 0):
        num = num // 5
        count += num
    return count

print(countTrailingZeros(100))