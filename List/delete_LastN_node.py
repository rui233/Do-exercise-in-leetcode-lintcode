def delete_last_N_node(self, n):
        '''删除链表中倒数第N个节点.
        主体思路：
            设置快、慢两个指针，快指针先行，慢指针不动；当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
            当快指针到达链表尾部的时候，慢指针所指向的就是链表的倒数第N个节点
        参数:
            n:需要删除的倒数第N个序数
        '''
        fast = self.__head
        slow = self.__head
		tmp = self.__head
        step = 0
        count = 0

        while step <= n:
            fast = fast.next
            step += 1

        while fast.next != None:
            fast = fast.next
            slow = slow.next
			count += 1
	        while count >= 1:
		        tmp = tmp.next

        tmp.next = slow.next