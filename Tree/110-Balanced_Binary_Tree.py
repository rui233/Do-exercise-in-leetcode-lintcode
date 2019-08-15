# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
#
class Solution(object):
    def isBalanced(self, root):
        height = self.get_height(root)
        return height != -1

    def get_height(self, root):
        if not root: return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if left == -1 or right == -1: return -1
        if abs(left - right) > 1:  return -1
        return max(left, right) + 1