class Solution:
	def levelOrderBottom(self,root):
		"""

		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if root is None:
			return []

		result,current = [],[root]

		while current:
			next_level,vals = [],[]
				vals.append(node.val)
				if node.left:
					next_level.append(node.left)
				if node.right:
					next_level.append(node.right)
				current = next_level
				result.append(vals)
			return result[::-1]