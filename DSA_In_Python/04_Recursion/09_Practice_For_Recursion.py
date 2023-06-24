
def fun(n):
    if n <= 1:
        return 0
    return 1 + fun(n//2)

print(fun(16))

"""
    fun(16)
        fun(8)
            fun(4)
                fun(2)
                    fun(1)
                    0
                0+1=1
            1+1=2
        1+2=3
    1+3=4
    return 4
"""