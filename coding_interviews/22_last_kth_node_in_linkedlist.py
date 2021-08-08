# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = head
        fast = head

        while fast and k > 0:
            fast = fast.next
            k -= 1

        if k > 1:
            return None

        while fast:
            fast = fast.next
            slow = slow.next

        return slow

