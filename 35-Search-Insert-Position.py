#Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You may assume no duplicates in the array.

#Example 1:
#Input: [1,3,5,6], 5      Output: 2
#first solution
class Solution:
    def searchInsert(self, array, target):
        for i in range(0, len(array)):

            if array[i] >= target:
                return i

        return len(array)

#second solution
class Solution:
    def searchInsert(self, n, t):

        if t in n:
            return n.index(t)
        else:
            n.append(t)
            return sorted(n).index(t)
