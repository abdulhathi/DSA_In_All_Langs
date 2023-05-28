def factorial(num):
    fact = 1
    while (num > 0):
        fact *= num
        num -= 1
    return fact

print(factorial(6))
print(factorial(100))
