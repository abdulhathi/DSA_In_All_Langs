def fun(n):
    if n == 0:
        return 
    fun(n-1)
    print(n, end=",")
    fun(n-1)

fun(3)
"""
    fun(3)
        fun(2)
            fun(1)
                fun(0)
                print 1
                fun(0)
            print 2
            fun(1)
                fun(0)
                print 1
                fun(0)
        print 3
        fun(2)
            fun(1)
                fun(0)
                print 1
                fun(0)
            print 2
            fun(1)
                fun(0)
                print 1
                fun(0)
    
O/P: 1,2,1,3,1,2,1
"""