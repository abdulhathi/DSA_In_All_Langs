# Basics of List in python

# List declaration
fruits = ["Apple", "Orange", "Banana", "Grapes"]
print(fruits)

# Lenght of the list
print(len(fruits))

# List data structure with different data types
fruits = ["Apple", "Orange"]
numbers = [1, 2, 3, 4, 5]
flags = [True, False, False]
print(fruits, numbers, flags)

# List data structure with different values
listItems = ["Abdul", 123, True, 13.10]
print(listItems)

# Print the list data type
print(type(listItems))

fruits1 = fruits
fruits1[0] = "Strawberri"
print(fruits1, fruits)

print(fruits[:])
fruits2 = fruits[:]
for c in (fruits,fruits1,fruits2):
    print(c)