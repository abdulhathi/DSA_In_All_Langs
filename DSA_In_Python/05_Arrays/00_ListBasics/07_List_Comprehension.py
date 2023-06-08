thisList = ["apple", "banana", "cherry", "orange"]
# Create a new list using for loop
fruits = []
for fruit in thisList:
	if "a" in fruit:
		fruits.append(fruit)
print(fruits)

# Create a new list using the list comprehension
fruits = [fruit for fruit in thisList if "e" in fruit]
print(fruits)

# Print fruits other than "Apple" using comprehension method
print([fruit for fruit in thisList if fruit != "apple"])

# Print fruits comprehension and ternery
print([x if x != "orange" else "its orange" for x in thisList])