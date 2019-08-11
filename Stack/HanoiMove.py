class HanoiMove:
	def __init__(self, stackNum, stackFrom, stackTo):
		'''
		stackNum 表示铁饼数量，stackFrom，stackTo表示铁饼从哪里转移到哪里
		'''
		if stackNum <= 0 or stackFrom == stackTo or stackFrom < 0 or stackTo < 0:
			raise RuntimeError("Invalid parameters")

		self.stackFrom = stackFrom
		self.stackTo = stackTo
		self.hanoiMove = []
		self.moveHanoiStack(self.stackFrom, self.stackTo, 1, stackNum)

	def printMoveSteps(self):
		if len(self.hanoiMove) == 1:
			print(self.hanoiMove.pop())
			return
		'''
		在输出第n个铁饼的挪动路径前，先输出前n-1个铁饼的挪动路径,最后再输出第n个铁饼的移动路径
		'''
		s = self.hanoiMove.pop()
		self.printMoveSteps()
		print(s)

	def moveHanoiStack(self, stackFrom, stackTo, top, bottom):
		'''
		top表示当前挪动铁饼的最高那块铁饼所在位置，bottom表示挪动铁饼的最低那块铁饼所在位置
		把杆子1上三块铁饼挪到杆子2上，对应的调用就是moveHanoiStack(1, 2, 1, 3)
		'''
		s = "Moving ring " + str(bottom) + " from stack " + str(stackFrom) + " to " + str(stackTo)
		if bottom - top == 0:
			# 如果只挪动一块铁饼，那么直接挪到目的地
			self.hanoiMove.append(s)
			return

		other = stackFrom
		for i in range(1, 4):
			# i表示杆子的编号
			if i != stackFrom and i != stackTo:
				# 找到用于中转的杆子编号
				other = i
				break
		# 先把n-1块铁饼挪到中转杆子
		self.moveHanoiStack(stackFrom, other, top, bottom - 1)
		# 把最后一块铁饼挪到指定杆子
		self.hanoiMove.append(s)
		# 把中转杆子上的n-1块铁饼挪到目的杆子
		self.moveHanoiStack(other, stackTo, top, bottom - 1)