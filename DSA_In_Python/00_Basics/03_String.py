
txt = "Hello World"
print(txt[0:5])
print(txt[2:5])

# Strip
txt = " Hello World "
print(f"-{txt}-")
print(f"-{txt.strip()}-")

# Upper case
print(txt.upper())
# Lower case
print(txt.lower())

# Replace
print(txt.replace("H","J"))

# Place holder
age = 39
s = "old"
txt = "My name is Abdul. I am {} years {}"
print(txt.format(age, s))