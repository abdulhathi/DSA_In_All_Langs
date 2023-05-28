thisList = ["apple", "banana", "cherry"]
# Loop the items in the list
for item in thisList:
	print(item)

# Loop the items in the list using index
for i in range(len(thisList)):
	print(thisList[i])

# While loop to iterate items in the list
i = 0
while i < len(thisList):
	print(thisList[i])
	i += 1

# Looping the items using comprehension
[print(f"Item - {item}") for item in thisList]