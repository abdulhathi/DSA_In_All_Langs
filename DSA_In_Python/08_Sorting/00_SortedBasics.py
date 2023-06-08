# Sorted to sort a int list
li = [4,3,7,3,6,2]
print(sorted(li))

# Sorted using custom function
li = [10,-15,-2,3]
def absSort(x):
    return abs(x)
print(sorted(li, key=absSort))
print(sorted(li, key=absSort, reverse=True))

# Sort the (List, Tuple, set, string, dictionary) using the Sorted function
tp = (6,2,4,9,3)
listResult = sorted(tp)
print(listResult)

set1 = {3,2,4,1,5,9}
liRes = sorted(set1)
print(liRes)

st = "Abdul Hathi"
liRes = sorted(st)
print(liRes)

dic = {4: "Abdul", 2: "Aysha", 10: "Amira", 5: "Afraz"}
keyRes = sorted(dic)
print(keyRes)

# list of tuples with each tuple contains two elements
tp1 = [(3,2),(4,5),(2,4)]
liRes = sorted(tp1)
print(liRes)