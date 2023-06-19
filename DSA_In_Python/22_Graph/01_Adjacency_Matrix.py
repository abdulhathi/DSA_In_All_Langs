"""
    (0)-----(1)
     |     /
     |    /
     |   /
     |  /
     | /
    (2)-----(3) 
"""

adjMatrix = [[0,1,1,0],
             [1,0,1,0],
             [1,1,0,1],
             [0,0,1,0]]

# check "U" and  "V" are adjacent - 
def checkAdjacent(u, v, adjMatrix):
    return adjMatrix[u][v] == 1
print(checkAdjacent(2,1,adjMatrix))

def findAllVerticesOfU(u, adjMatrix):
    return adjMatrix[u]
print(findAllVerticesOfU(2, adjMatrix))

def findDegreeOfU(u, adjMatrix):
    return sum(adjMatrix[u])
print(findDegreeOfU(2, adjMatrix))