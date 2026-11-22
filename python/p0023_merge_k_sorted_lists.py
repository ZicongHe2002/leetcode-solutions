from heapq import heappop, heappush



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeKLists(self, lists):
        heap = []
        for index, node in enumerate(lists):
            if node is not None:
                heappush(heap, (node.val, index, node))
        dummy = ListNode()
        tail = dummy
        while heap:
            _, index, node = heappop(heap)
            following = node.next
            tail.next = node
            tail = node
            if following is not None:
                heappush(heap, (following.val, index, following))
        tail.next = None
        return dummy.next
