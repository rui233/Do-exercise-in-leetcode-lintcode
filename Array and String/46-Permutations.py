class Solution:
	def permute(self,nums):
		"""

		:type nums:List[int]
		:rtype: List[List[int]]
		"""

		if len(nums) <= 1:
			return [nums]

		answer = []
		for i,nums in enumerate(nums):
			n = nums[:i] + nums[i+1: ]
			for y in self.permute(n):
				answer.append([nums] + y )

		return answer