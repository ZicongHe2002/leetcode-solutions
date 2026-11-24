class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        clones = {}
        current = head
        while current is not None:
            clones[current] = Node(current.val)
            current = current.next
        current = head
        while current is not None:
            clones[current].next = clones.get(current.next)
            clones[current].random = clones.get(current.random)
            current = current.next
        return clones.get(head)
