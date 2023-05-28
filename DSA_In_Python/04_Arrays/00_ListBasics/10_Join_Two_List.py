# Join two list using (+) opertor
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

newList = list1 + list2
print(newList)

# Join two list using for loop
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for item in list2:
  list1.append(item)
print(list1)

# Join two list using extend method
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)