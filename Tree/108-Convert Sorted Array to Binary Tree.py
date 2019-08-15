class Solution:
	def sortedArrayToBST(self,nums):
		"""

		:type nums:List[int]
		:rtype: TreeNode
		"""
	def to_bst(nums,start,end):
		if start > end:
			return None
		mid = (start + end) // 2
		node = TreeNode(nums[mid])
		node.left = to_bst(nums,start,mid-1)
		node.right = to_bst(nums,mid+1,end)
		return node

	return to_bst(nums,0, len(nums) -1 )