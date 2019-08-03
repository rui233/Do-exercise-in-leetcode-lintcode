#递归法
class ListReverse:
    def __init__(self, head):
        self.listHead = head
        self.newHead = None
    def recursiveReverse(self, node):
        #如果队列为空或者只有一个节点，那么队列已经倒转完成
        if node is None or node.next is None:
            self.newHead = node
            return node
        '''
        如果队列包含多个节点，那么通过递归调用的方式，先把当前节点之后所有节点实现倒转，
        然后再把当前节点之后节点的next指针指向自己从而完成整个列表所有节点的导致
        '''
        head = self.recursiveReverse(node.next)
        head.next = node
        node.next = None
        return node
    def getReverseList(self):
        '''
        listHead是原队列头节点，执行recursiveReverse后newHead指向新列表的头结点，它
        对应的其实是原列表的尾节点，而head指向新列表的尾节点
        '''
        self.recursiveReverse(self.listHead)
        return self.newHead

# Reverse singly-linked list
# 单链表反转
# Note that the input is assumed to be a Node, not a linked list.
def reverse(head: Node) -> Optional[Node]:
    reversed_head = None
    current = head
    while current:
        reversed_head, reversed_head._next, current = current, reversed_head, current._next
    return reversed_head


#插入法：从第二个节点开始，把遍历到的结点插入到头结点的后面

def Reverse(head):
    #判断链表是否为空
	if head is None or head.next is None:
		return head
	cur = None
    next = None
    cur = head.next.next
    head.next.next = None#设置第一个结点为尾结点
    while cur is not None:
	    next = cur.next
	    cur.next = head.next
	    head.next = cur
	    cur = next