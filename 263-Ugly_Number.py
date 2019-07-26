#Write a program to check whether a given number is an ugly number.

#Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

#Input: 6
#Output: true
#Explanation: 6 = 2 × 3



def isUgly(self, num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 0:
        return False
    for x in [2, 3, 5]:
        while num % x == 0:
            num = num / x
    return num == 1