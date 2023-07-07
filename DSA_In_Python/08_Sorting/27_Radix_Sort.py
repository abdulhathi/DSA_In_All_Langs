from collections import defaultdict

def radixSort(arr):
    divisor = 1
    maxlen = len(str(max(arr)))

    countDic = defaultdict(list)
    while maxlen > 0:
        for num in arr:
            pos = (num // divisor) % 10
            countDic[pos].append(num)
        arr = []
        for key in range(10):
            arr += countDic[key]
        countDic = defaultdict(list)
        divisor = divisor * 10
        maxlen -= 1
    
    return arr

print(radixSort([319,212,6,8,100,50]))



# print(152 % 10)

# print((152//10) % 10)

# print((152//100) % 10)
