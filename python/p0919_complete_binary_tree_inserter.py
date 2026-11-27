from collections import deque


class CBTInserter:
    def __init__(self, root):
        self.root = root
        self.available = deque()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left is None or node.right is None:
                self.available.append(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def insert(self, val):
        node = TreeNode(val)
        parent = self.available[0]
        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
            self.available.popleft()
        self.available.append(node)
        return parent.val

    def get_root(self):
        return self.root
