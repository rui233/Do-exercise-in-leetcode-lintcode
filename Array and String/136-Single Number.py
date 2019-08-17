# Given a non-empty array of integers,every element appears twice except for one.
# Find that single one
# should have linear runtime complexity,without extra memory

class Solution(object):
	def singleNumber(self,nums):
		"""

		:type nums:List[int]
		:rtype: int
		"""

		ans = 0

		for num in numbers:
			ans ^= num

		return ans