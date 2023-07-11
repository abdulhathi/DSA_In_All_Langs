import math

def ropeCutting(cuts, ropeLength):

    def topDown(length):
        if length < 0:
            return -math.inf
        if length == 0:
            return 0
        maxPiece = -math.inf
        for cut in cuts:
            # if length - cut < 0:
            #     continue
            maxPiece = max(maxPiece, 1 + topDown(length - cut))
        return maxPiece
    
    res = topDown(ropeLength)
    return -1 if res == -math.inf else res


print(ropeCutting([1,2,3], 5))
print(ropeCutting([12,11,13], 23))
print(ropeCutting([2,4,2], 3))
