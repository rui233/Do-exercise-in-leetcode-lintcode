class LNode:
	def __new__(self,x):
		self.data = x
		self.next = None
#对不带头结点的单链表翻转
    def Reverse(head):
		if head==None or head.next ==None;
			return head
		pre = head
		cur = head.next
		next = cur.next
		pre.next = None
		#使当前遍历到的结点cur指向其前驱结点
		while cur!=None:
			next = cur.next
			cur.next = pre
			pre = cur
			cur = cur.next
			cur = next

		return pre

	#对链表K翻转
	def ReverseK(head,k):
		if head==None or head.next == None or k<2:
			return
		i=1
		pre=head
		begin=head.next
		end=None
		pNext = None
		while begin!=None:
			end = begin

			while i<k:
				if end.next!=None:
					end = end.next
				else:
					return
				i+=1
				pNext=end.next
				end.next=None
				pre.next=Reverse(begin)
				begin.next=pNext
				pre=begin
				begin=pNext
				i=1
if __name__=="__main__":
	i=1
	head=LNode()

	head.next=None
	tmp=None
	cur=head
	while i<8:
		tmp = LNode()
		tmp.data = i
		tmp.next=None
		cur.next=tmp
		cur=tmp
		i+=1
	print ("顺序输出:,")
	cur=head.next
	while cur!=None:
		print(cur.data)
		cur=cur.next
		ReverseK(head,3)
		print ("\n逆序输出:,")
		cur = head.next
		while cur!=None:
			print (cur.data)
			cur=cur.next
		cur=head.next
		while cur!=None:
			tmp=cur
			cur=cur.next

