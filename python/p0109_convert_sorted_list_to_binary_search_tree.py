class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortedListToBST(self, head):
        length = 0
        cursor = head
        while cursor is not None:
            length += 1
            cursor = cursor.next
        cursor = head

        def build(size):
            nonlocal cursor
            if size == 0:
                return None
            left_size = size // 2
            left = build(left_size)
            root = TreeNode(cursor.val)
            cursor = cursor.next
            root.left = left
            root.right = build(size - left_size - 1)
            return root

        return build(length)
