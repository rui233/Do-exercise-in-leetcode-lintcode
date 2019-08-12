# Given n pairs of parentheses,write a function to generate all combination
# of well-formed parentheses.

class Solution:
	def generateParenthesis(selfself,n):
		"""

		:type n:int
		:rtype: List[str]
		"""
		if n == 0:
			return []

		result = []
		self.helper(n,n,'',result)
		return result

	def helper(selfself,l,r,item,result):
		if r < l:
			return
		if l == 0 and r ==0:
			result.append(item)
		if l > 0:
			self.helper(l-1,r,item + '(',result)
		if r >0:
			self.helper(l,r-1,item + ')',result)