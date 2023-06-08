# Sort() function - Sort the list itself
l1 = [10,3,4,1,20]
l1.sort()
print(l1)

# Sorted() function - Sorted function returns a new sorted list.
l1 = [10,3,4,1,20]
l2 = sorted(l1)
print(l2)

# Sort in reverse
l1 = [10,3,4,1,20]
l1.sort(reverse=True)
print(l1)

# Sort the string list
l1 = ["Cat", "Tiger", "Lion", "Rat"]
l1.sort()
print(l1)

# Custome sorting using fucntions
l1 = ["Rat", "Cat", "Tiger", "Lion", ]
def mySortFun(s):
    return len(s)
l1.sort(key = mySortFun)
print(l1)
l1.sort(key = mySortFun, reverse = True)
print(l1)

# Sorting user defined objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def sortPoint(p):
    return p.x

points = [Point(5,15), Point(25, 23), Point(5,23)]
points.sort(key=sortPoint)
print([(p.x,p.y) for p in points])

# Magic methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.y

points = [Point(1,15), Point(10,5), Point(1,8)]
points.sort()
print([(p.x,p.y) for p in points])