newList = list(("Abdul", 39, "Male", "Technical Lead","California","-","-"))
# Remove/Delete an item in the list
newList.remove("California")
print(newList)

# Remove/Delete an item in the list specified index
newList.pop(4)
print(newList)

# Remove/Delete a last item in the list
popVal = newList.pop()
print("Popedup value : ", popVal)
print(newList)

# del keyword to Remove/Delete an item in the list specified index
del newList[3]
print(newList)

# Del kewy to remove/Delete items in the range
li = [1,2,3,4,5,6]
del li[2:4]
print(li)

# Clear all items in the list
newList.clear()
print(newList)

# del keyword to delete the list object
del newList
try:
	print(newList)
except NameError as ex:
	print(ex)