class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root):
        if root is None:
            return None
        leftmost = root
        while leftmost.left is not None:
            current = leftmost
            while current is not None:
                current.left.next = current.right
                current.right.next = current.next.left if current.next is not None else None
                current = current.next
            leftmost = leftmost.left
        return root
