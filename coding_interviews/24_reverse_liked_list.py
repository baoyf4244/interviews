class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        nxt = None

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre


head = ListNode(1)
for i in range(2, 6):
    head.next = ListNode(i)

node = Solution().reverseList(head)