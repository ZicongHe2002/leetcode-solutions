class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA, headB):
        left, right = headA, headB
        while left is not right:
            left = headB if left is None else left.next
            right = headA if right is None else right.next
        return left
