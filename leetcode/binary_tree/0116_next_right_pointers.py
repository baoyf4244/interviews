
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        self.connect_two_node(root.left, root.right)
        return root

    def connect_two_node(self, left, right):
        if not left or not right:
            return
        left.next = right

        self.connect_two_node(left.left, left.right)
        self.connect_two_node(right.left, right.right)
        self.connect_two_node(left.right, right.left)
