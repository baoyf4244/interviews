class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def get_next(node):
    if not node:
        return None

    next_node = None
    if node.right:
        cur_node = node.right
        while cur_node:
            next_node = cur_node
            cur_node = cur_node.left
        return next_node

    if node.parent:
        if node.parent.left == node:
            return node.parent

        if node.parent.right == node:
            cur_node = node.parent
            while cur_node and cur_node.parent.left != cur_node:
                cur_node = cur_node.parent
            return cur_node.parent
    return None

