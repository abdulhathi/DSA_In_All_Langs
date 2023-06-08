import math

# TIME : O(N) SPACE : O(1)
def getSecMax(nums):
  fLar, sLar = nums[0], -math.inf
  for i in range(1, len(nums)):
    if nums[i] == fLar:
      continue
    if nums[i] > fLar:
      sLar = fLar
      fLar = nums[i]
    else:
      sLar = max(nums[i], sLar)
  return fLar, None if sLar == -math.inf else sLar

print(getSecMax([10,5,8,20]))
print(getSecMax([20,10,20,8,12]))
print(getSecMax([10,10,10]))