def find_mid_node(self):
        '''查找链表中的中间节点.
        主体思想:
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，则当快指针到达链表尾部的时候，慢指针指向链表的中间节点
        返回:
            node:链表的中间节点
        '''
        fast = self.__head
        slow = self.__head

        while fast.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow