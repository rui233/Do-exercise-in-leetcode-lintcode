# Description:
# 针对小括号（），给定一个小括号字符串，判断左右括号是否匹配

class ParenMatch:
	def __init__(self, parens):
		self.parens = parens
		self.stack = []

	def isMatch(self):
		for c in self.parens:
			if c == '(':
				# 读取左括号则压入堆栈
				self.stack.append(c)
			elif c == ')':
				# 读取右括号则弹出堆栈，如果堆栈为空，括号就不匹配
				if len(self.stack) == 0:
					return False
				self.stack.pop()
			else:
				raise RuntimeError("Illegal character")
		# 所有字符读取完后，堆栈不为空，那么括号不匹配
		if len(self.stack) != 0:
			return False

		return True