class StackSorter:
	def __init(self):
		pass

	def sortByRecursion(self, stack):
		if (len(stack) == 0):
			return stack
		# 先把弹出的元素寄存在调用堆栈上
		v = stack.pop()
		# 递归的排序余下的元素
		stack = self.sortByRecursion(stack)
		# 递归的把元素按顺序插入堆栈
		stack = self.insert(stack, v)

		return stack

	def insert(self, stack, val):
		if (len(stack) == 0 or val <= stack[len(stack) - 1]):
			# 如果插入的值比栈顶元素小，那么只讲将元素压入栈顶
			stack.append(val)
			return stack
		# 把小于val的元素暂存在调用堆栈上
		t = stack.pop()
		# 递归性的将元素插入余下的堆栈元素
		self.insert(stack, val)
		# 再把暂存的元素插回到堆栈
		stack.append(t)
		return stack