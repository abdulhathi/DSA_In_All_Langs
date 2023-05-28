# TIME : O(n) SPACE : O(1)
def average(nums):
  sumOfNums = 0
  for num in nums:
    sumOfNums += num
  return sumOfNums / len(nums)

print(average([10,20,30,40]))
print(average([30,60,40]))