from collections import deque



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def widthOfBinaryTree(self, root):
        queue = deque([(root, 0)])
        best = 0
        while queue:
            offset = queue[0][1]
            for _ in range(len(queue)):
                node, index = queue.popleft()
                index -= offset
                if node.left is not None:
                    queue.append((node.left, 2 * index))
                if node.right is not None:
                    queue.append((node.right, 2 * index + 1))
            best = max(best, index + 1)
        return best
