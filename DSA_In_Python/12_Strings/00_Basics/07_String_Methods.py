# Capitalize
print("abdul hathi".capitalize())

# CaseFold
print("ABDUL HATHI".casefold())

# center
print("abdul hathi".center(20))

# count
print("abdul hathi mohamed".count("a"))

# encode
print("abdul hathi".encode())

# endswith
print("abdul hathi".endswith("i"))

# find
print("abdul hathi".find("hat"))
print("abdul hathi".find("hatt"))

# index
print("mohamed hussain".index("amed"))

# right index
print("abdulhathi".rindex("a"))

# split method
path = "/home//foo/"
res = path.split("/")
for p in res:
    if p:
        print(p)

print("/../".split("/"))