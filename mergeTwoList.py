# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, m1: ListNode, m2: ListNode) -> ListNode:
        l1, l2 = m1, m2
        first = ListNode(0)
        head = first
        while True:
            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    head.val = l1.val
                    l1 = l1.next
                else:
                    head.val = l2.val
                    l2 = l2.next

            elif l1 is None and l2 is not None:
                head.val = l2.val
                l2 = l2.next
            elif l1 is not None and l2 is None:
                head.val = l1.val
                l1 = l1.next
            else:
                return first
            head.next = ListNode()
            head = head.next
