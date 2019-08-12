# Given a sorted array and a target value,return the index if the target is found.
# if not,return the index where it would be if it were inserted in order
# you may assume no duplicates in the array

class Solution:
	def searchInsert(self,nums,target):
		"""

		:type nums:List[int]
		:type target: int
		:rtype: int
		"""

		if target > nums[len(nums) - 1]:
			return len(nums)

		for i in range(len(nums)):
			if nums[i] >= target:
				return i



