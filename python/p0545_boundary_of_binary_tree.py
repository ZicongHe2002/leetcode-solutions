class Solution:
    def boundaryOfBinaryTree(self, root):
        def is_leaf(node):
            return node.left is None and node.right is None

        answer = [root.val]
        if is_leaf(root):
            return answer
        node = root.left
        while node is not None:
            if not is_leaf(node):
                answer.append(node.val)
            node = node.left if node.left is not None else node.right
        pending = [root]
        while pending:
            node = pending.pop()
            if is_leaf(node):
                answer.append(node.val)
            else:
                if node.right is not None:
                    pending.append(node.right)
                if node.left is not None:
                    pending.append(node.left)
        right = []
        node = root.right
        while node is not None:
            if not is_leaf(node):
                right.append(node.val)
            node = node.right if node.right is not None else node.left
        answer.extend(reversed(right))
        return answer
