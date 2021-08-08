from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next

        arr = []
        while stack:
            arr.append(stack.pop())

        return arr