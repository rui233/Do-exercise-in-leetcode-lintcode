#description:
# Given a sorted linked list,
# delete all duplicates such that each element appear only once.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicates(self, head):
		if head == None:
			return head

		node = head

		while node.next:
			if node.val == node.next.val:
				node.next = node.next.next
			else:
				node = node.next

		return head