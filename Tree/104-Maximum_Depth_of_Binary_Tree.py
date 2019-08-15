#Given a binary tree, find its maximum depth.

#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#Note: A leaf is a node with no children.

class Solution(object):
    def maxDepth(self, root):
        if not root: return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1