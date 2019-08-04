#在O（1）时间复杂度内删除单链表非末尾节点
def deleteNode(node):
    if node.next is None:
        return
    #把下一个节点的值拷贝到当前节点
    node.val = node.next.val
    #把当前节点的next指针指向下下个节点
    node.next = node.next.next
def showList(head):
    while head is not None:
        print("{0}->".format(head.val), end="")
        head = head.next
    print("null")