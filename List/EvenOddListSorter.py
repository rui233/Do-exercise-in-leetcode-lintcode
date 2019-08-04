class EvenOddListSorter:

	def sort(self):
		if head is None or head.next is None:
			return head
		# 将oddHead和evenHead分别指向首个奇数节点和偶数节点
		evenHead = head
		oddHead = head.next
		oddHeadCopy = oddHead
		evenTail = evenHead

		while evenHead is not None and oddHead is not None:
			# 把evenHead.next指向oddHead.next
			evenTail = evenHead
			evenHead.next = oddHead.next
			evenHead = evenHead.next
			# 把oddHead.next指向evenHead.next
			if evenHead is not None:
				evenTail = evenHead
				oddHead.next = evenHead.next
				oddHead = oddHead.next
		# 把偶数队列和奇数队列收尾相连
		evenTail.next = oddHeadCopy
		return head