def squareRoot(x):
    sqrt = 1
    for i in range(1, (x//2)+1):
        if (i*i) <= x:
            sqrt = max(sqrt, i)
    return sqrt

print(squareRoot(256))


def squareRootBinarySearch(x):
    lp, rp = 1, x//2
    sqrt = 1
    while lp <= rp:
        mid = (lp+rp)//2
        midSq = mid*mid
        if midSq <= x:
            sqrt = max(mid, sqrt)
            lp = mid+1
        else:
            rp = mid-1
    return sqrt

print(squareRootBinarySearch(256))