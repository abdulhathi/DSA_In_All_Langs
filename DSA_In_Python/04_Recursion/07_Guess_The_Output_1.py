def fun(n):
    if n == 0:
        return 
    print(n, end=",")
    fun(n-1)
    print(n, end=",")


# 3,2,1,1,2,3
fun(3)