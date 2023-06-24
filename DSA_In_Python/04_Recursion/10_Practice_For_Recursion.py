
def fun(n):
    if n == 0:
        return
    fun(n//2)
    print(n%2)

fun(13)

"""
    fun(13)
        fun(6)
            fun(3)
                fun(1)
                    fun(0)
                1
            1
        0
    1

    1101
"""