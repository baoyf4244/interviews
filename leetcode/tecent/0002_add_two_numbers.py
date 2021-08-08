# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        results = ListNode(0)
        results_cur = results
        temp = 0

        while cur1 and cur2:
            res = cur1.val + cur2.val + temp
            temp = res // 10
            results_cur.next = ListNode(res % 10)
            results_cur = results_cur.next
            cur1 = cur1.next
            cur2 = cur2.next

        if not cur1 and not cur2:
            if temp != 0:
                results_cur.next = ListNode(temp)
            return results.next
        cur = cur1 if cur1 else cur2

        while cur:
            res = cur.val + temp
            temp = res // 10
            results_cur.next = ListNode(res % 10)
            results_cur = results_cur.next
            cur = cur.next

        if temp != 0:
            results_cur.next = ListNode(temp)

        return results.next


