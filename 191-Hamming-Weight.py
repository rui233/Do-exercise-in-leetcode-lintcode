
def hammingWeight(self,n) {
    int c = 0
    while n:
        n &= n-1
        c += 1
    return c;
}
#时间复杂度为O（1的个数)
#x= x & x-1  表示把x二进制形式的最后一位打掉；然后循环