class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        slow = fast = head

        while k > 0:
            k -= 1
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        return slow
