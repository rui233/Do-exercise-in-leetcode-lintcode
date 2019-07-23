#Given a non-empty array of integers, return the k most frequent elements.
#Example 1:

#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]



from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        return heapq.nlargest(k, c,key=lambda x:c[x])


