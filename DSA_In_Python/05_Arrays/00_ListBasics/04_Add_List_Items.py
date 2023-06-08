# List data type declaration using list() constructor from tuples
newList = list(("Abdul", 39, "Male", "Technical Lead"))
print(newList)

# Append an item in the list
newList.append("California")
print(newList)

# Extend items in the list
newList.extend(["Bsc-Microbiologiest", "12-20-1989"])
print(newList)

# Adding Tuples in the list
tupleItems = ("VK.Pudur", "Hair-Black")
newList.extend(tupleItems)
print(newList)