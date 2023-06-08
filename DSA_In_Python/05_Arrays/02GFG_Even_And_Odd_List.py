def seperateEvenAndOdd(nums):
  even, odd = [], []
  for num in nums:
    if num % 2 == 0:
      even.append(num)
    else:
      odd.append(num)
  return even, odd

print(seperateEvenAndOdd([10,41,30,15,80]))
print(seperateEvenAndOdd([10,30,40]))

# Using list complrehension method
def seperateEvenAndOdd(nums):
  even = [num for num in nums if num % 2 == 0]
  odd = [num for num in nums if num % 2 != 0]
  return even, odd

print(seperateEvenAndOdd([10,41,30,15,80]))
print(seperateEvenAndOdd([10,30,40]))