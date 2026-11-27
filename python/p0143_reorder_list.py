class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reorderList(self, head):
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        current = slow.next
        slow.next = None
        previous = None
        while current is not None:
            following = current.next
            current.next = previous
            previous, current = current, following
        first, second = head, previous
        while second is not None:
            next_first, next_second = first.next, second.next
            first.next = second
            second.next = next_first
            first, second = next_first, next_second
