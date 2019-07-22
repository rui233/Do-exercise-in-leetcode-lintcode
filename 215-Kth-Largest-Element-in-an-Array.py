#Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#Example 1:

#Input: [3,2,1,5,6,4] and k = 2
#Output: 5

class Solution:
    def findKthLargest4(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in xrange(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

