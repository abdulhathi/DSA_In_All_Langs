# Sort method to sort ascending order
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()
print(thisList)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort method to sort descending order
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Sort using ascending order using key function
def myFunc(item):
    return abs(item - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myFunc)
print(thislist)

# Case intensive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# change the charecter case and sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

