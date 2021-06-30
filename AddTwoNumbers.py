class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    node1 = l1
    node2 = l2
    extra = 0
    li = []
    while True:
        if node1 is not None and node2 is not None:
            temp = node1.val + node2.val + extra
            extra = int(temp / 10)
            node1 = node1.next
            node2 = node2.next
        elif node1 is not None and node2 is None:
            temp = node1.val + extra
            extra = int(temp / 10)
            node1 = node1.next

        elif node1 is None and node2 is not None:
            temp = node2.val + extra
            extra = int(temp / 10)
            node2 = node2.next
        else:
            if extra == 0:
                break
            else:
                temp = extra
                extra = 0
                print(f'node1: None  node2: None sum: {temp}   extra:{extra}')
        li.append(ListNode(temp % 10))

    for i in range(0, len(li) - 1):
        li[i].next = li[i + 1]
    return li[0]