class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root):
        dummy = Node()
        level = root
        while level is not None:
            dummy.next = None
            tail = dummy
            current = level
            while current is not None:
                if current.left is not None:
                    tail.next = current.left
                    tail = current.left
                if current.right is not None:
                    tail.next = current.right
                    tail = current.right
                current = current.next
            tail.next = None
            level = dummy.next
        return root
