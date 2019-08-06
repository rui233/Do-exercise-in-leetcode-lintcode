# Description:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:

def __init__(self):
    self.stack = []

# @param x, an integer
# @return an integer
def push(self, x):
    curMin = self.getMin()
    if curMin == None or x < curMin:
        curMin = x
    self.stack.append((x, curMin));

# @return nothing
def pop(self):
    self.stack.pop()


# @return an integer
def top(self):
    if len(self.stack) == 0:
        return None
    else:
        return self.stack[-1][0]


# @return an integer
def getMin(self):
    if len(self.stack) == 0:
        return None
    else:
        return self.stack[-1][1]