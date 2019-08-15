
# Using one Queue
import collections

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = collections.deque([])

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

        self.stack.popleft()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0

# Using two queues

from queue import Queue


class Stack2:

	def __init__(self):

		# Two inbuilt queues
		self.q1 = Queue()
		self.q2 = Queue()

		# To maintain current number
		# of elements
		self.curr_size = 0

	def push(self, x):
		self.curr_size += 1

		# Push x first in empty q2
		self.q2.put(x)

		# Push all the remaining
		# elements in q1 to q2.
		while (not self.q1.empty()):
			self.q2.put(self.q1.queue[0])
			self.q1.get()

		# swap the names of two queues
		self.q = self.q1
		self.q1 = self.q2
		self.q2 = self.q

	def pop(self):

		# if no elements are there in q1
		if (self.q1.empty()):
			return
		self.q1.get()
		self.curr_size -= 1

	def top(self):
		if (self.q1.empty()):
			return -1
		return self.q1.queue[0]