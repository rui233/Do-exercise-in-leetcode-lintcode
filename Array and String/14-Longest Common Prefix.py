# 1
class Solution1:
	def longestCommonPrefix(self,strs):
		"""

		:type strs:List[str]
		:rtype: str
		"""
		if not strs:
			return ""

		for i in range(len(strs[0])):
			for string in strs[1:]:
				if i >= len(string) or string[i] != strs[0][i]:
					return strs[0][:i]

		return strs[0]


#  2
class Solution2:
	def longestCommonPrefix(self,strs):
		"""

		:type strs:List[str]
		:rtype: str
		"""
		result = ""
		i = 0

		while True:
			try:
                strsets = set(string[i] for string in strs)
				print('sets',sets)
			    if len(sets) == 1:
				    result += strsets.pop( )
					i += 1
			except Exception as e:
				break

		return result