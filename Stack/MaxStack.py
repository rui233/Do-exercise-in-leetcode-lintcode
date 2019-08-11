import sys


class MaxStack:
	def __init__(self):
		self.stack = []
		self.maxStack = []
		self.maxVal = -sys.maxsize - 1

	def push(self, val):
		if val > self.maxVal:
			self.maxVal = val
			self.maxStack.append(val)

		self.stack.append(val)

	def peek(self):
		# 返回堆栈最顶元素但不弹出
		return self.stack[len(self.stack) - 1]

	def pop(self):
		# 如果弹出的元素是当前堆栈最大值，那么也要将maxStack顶部的元素弹出
		if self.peek() == self.maxVal:
			self.maxStack.pop()
		self.maxVal = self.maxStack[len(self.maxStack) - 1]

		return self.stack.pop()

	def max(self):
		return self.maxStack[len(self.maxStack) - 1]