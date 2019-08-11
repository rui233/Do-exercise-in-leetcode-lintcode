# Input:[1,2,3] to Output:[1,2,4]
# Input :[2,9] to Output:[3,0]
# 最后一位进一

class Solution:
	def plusOne(selfself,digits):
		'''

		:type digits:List[int]
		:rtype: List[int]
		'''
		for i in reversed(range(len(digits))):
			if digits[i] == 9:
				digits[i] = 0
			else:
				digits[i] += 1
				return digits
			digits[0] = 1
			digits.append(0)
			return digits
