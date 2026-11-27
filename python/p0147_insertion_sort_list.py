class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def insertionSortList(self, head):
        dummy = ListNode()
        current = head
        while current is not None:
            following = current.next
            before = dummy
            while before.next is not None and before.next.val <= current.val:
                before = before.next
            current.next = before.next
            before.next = current
            current = following
        return dummy.next
