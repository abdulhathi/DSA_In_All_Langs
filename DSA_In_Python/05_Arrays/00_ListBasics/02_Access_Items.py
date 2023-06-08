newList = ["Abdul", 39, "Male", "Technical Lead"]
# Access item in list
print(newList[0], newList[3])
print(newList[-1])
print(newList[1:])

# Print items in reverse order
print(newList[-4:-1])

# Check an item if exist or not
if "34" in newList:
  print(f"34 is exist in the list")
  
# Index an item in the new list
print(newList.index(39))

# Index to find an item between the range
try:
	li = [1,2,2,2,2,3,4,5,5]
	print(li.index(2, 5,9))
except ValueError as ex:
  print(ex, "between the range from index 5 to 9.")

# Count number of items in the list
li = [1,2,2,2,2,3,4,5,5]
print(li.count(2))

