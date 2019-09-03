class Solution:
	def findContentChildren(self, g: List[int], s: List[int]) -> int:
		
		g.sort()
		s.sort()
		i = 0
		j = 0
		res = 0
		while i <= len(g) and j <= len(s):
			if s[j] < g [i]:
				j += 1
			else:
				i += 1
				j += 1
				res += 1
			return res
