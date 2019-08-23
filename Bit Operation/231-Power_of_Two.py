def isPowerOfTwo(self,n):
    return n > 0 and not (n & n-1)
#2^n   其中(n & n-1 )的值为0 、and not 为逻辑运算符