class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):
        less_dummy = ListNode()
        rest_dummy = ListNode()
        less_tail, rest_tail = less_dummy, rest_dummy
        current = head
        while current is not None:
            following = current.next
            current.next = None
            if current.val < x:
                less_tail.next = current
                less_tail = current
            else:
                rest_tail.next = current
                rest_tail = current
            current = following
        less_tail.next = rest_dummy.next
        return less_dummy.next
