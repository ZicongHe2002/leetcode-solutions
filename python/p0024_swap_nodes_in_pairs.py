class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        previous = dummy
        while previous.next is not None and previous.next.next is not None:
            first = previous.next
            second = first.next
            first.next = second.next
            second.next = first
            previous.next = second
            previous = first
        return dummy.next
