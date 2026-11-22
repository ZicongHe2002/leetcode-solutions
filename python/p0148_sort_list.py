class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def sortList(self, head):
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next

        def split(start, width):
            if start is None:
                return None
            for _ in range(width - 1):
                if start.next is None:
                    break
                start = start.next
            remaining = start.next
            start.next = None
            return remaining

        dummy = ListNode(0, head)
        width = 1
        while width < length:
            tail, current = dummy, dummy.next
            while current is not None:
                left = current
                right = split(left, width)
                current = split(right, width)
                while left is not None and right is not None:
                    if left.val <= right.val:
                        tail.next = left
                        left = left.next
                    else:
                        tail.next = right
                        right = right.next
                    tail = tail.next
                tail.next = left if left is not None else right
                while tail.next is not None:
                    tail = tail.next
            width *= 2
        return dummy.next
