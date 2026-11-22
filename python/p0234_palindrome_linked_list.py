class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def _reverse(head):
        previous = None
        while head is not None:
            following = head.next
            head.next = previous
            previous = head
            head = following
        return previous

    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        first_half_end = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            first_half_end = first_half_end.next
            fast = fast.next.next
        reversed_half = self._reverse(first_half_end.next)
        left, right = head, reversed_half
        matches = True
        while right is not None:
            if left.val != right.val:
                matches = False
            left = left.next
            right = right.next
        first_half_end.next = self._reverse(reversed_half)
        return matches
