class ReversePolishExpr:
	def __init__(self, expr):
		self.expression = expr
		self.stack = []

	def calculation(self):
		exprs = self.expression.split(',')
		for expr in exprs:
			if self.isOperator(expr) and len(self.stack) < 2:
				raise RuntimeError('stack less than 2 elements')
			if self.isOperator(expr):
				# 如果当前字符是操作符，那么将堆栈顶部两元素弹出后进行计算
				self.doCalculation(expr)
			else:
				# 如果当前字符是数字，将其压入堆栈
				self.stack.append(int(expr))

		return self.stack.pop()

	def isOperator(self, expr):
		if len(expr) > 1:
			return False
		if expr == "+" or expr == "-" or expr == "*" or expr == "/":
			return True
		return False

	def doCalculation(self, operator):
		'''
		如果当前读入是操作符，弹出堆栈顶部的两个元素，根据操作符进行计算，再把结果压入堆栈
		'''
		op1 = self.stack.pop()
		op2 = self.stack.pop()

		if operator == "+":
			self.stack.append(op1 + op2)
		elif operator == "-":
			self.stack.append(op1 - op2)
		elif operator == "*":
			self.stack.append(op1 * op2)
		elif operator == "/":
			self.stack.append(op1 / op2)

