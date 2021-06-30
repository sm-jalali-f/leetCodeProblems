# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2
        result = []
        while not (n1 is None and n2 is None):
            if n1 is None:
                result.append(ListNode(n2.val))
                n2 = n2.next
            elif n2 is None:
                result.append(ListNode(n1.val))
                n1 = n1.next
            else:
                if n1.val <= n2.val:
                    result.append(ListNode(n1.val))
                    n1 = n1.next
                else:
                    result.append(ListNode(n2.val))
                    n2 = n2.next

        for i in range(0, len(result) - 1):
            result[i].next = result[i + 1]
        if len(result) > 0:
            return result[0]
        else:
            return None


s = Solution()
temp = ListNode(4)
l1 = ListNode(2, temp)
temp = ListNode(1, l1)
l1 = temp

temp = ListNode(4)
l2 = ListNode(3, temp)
temp = ListNode(1, l2)
l2 = temp

res = s.mergeTwoLists(None, None)
while res is not None:
    print(res.val)
    res = res.next
