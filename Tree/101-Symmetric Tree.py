class Solution:
	def isSymmetric(selfself,root):
		"""

		:type root:TreeNode
		:rtype: bool
		"""
		if root is None:
			return True

		return self.isSymmetricRecu(root.left,root.right)
	def isSymmetricRecu(self,left,right):
		if left is None and right is None:
			return True
		if left is None or right is None or left.val !=right.val:
			return False
		return self.isSymmetricRecu(left.left,right.right) and self.isSymmetricRecu(left.right,right.left)
