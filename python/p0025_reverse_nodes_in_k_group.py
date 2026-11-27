class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        before = dummy
        while True:
            end = before
            for _ in range(k):
                end = end.next
                if end is None:
                    return dummy.next
            after = end.next
            first = before.next
            previous, current = after, first
            while current is not after:
                following = current.next
                current.next = previous
                previous, current = current, following
            before.next = end
            before = first
