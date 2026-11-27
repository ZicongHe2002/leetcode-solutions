class Solution:
    def insert(self, head, insertVal):
        inserted = Node(insertVal)
        if head is None:
            inserted.next = inserted
            return inserted
        current = head
        while True:
            following = current.next
            ordinary = current.val <= insertVal <= following.val
            wrap = current.val > following.val and (insertVal >= current.val or insertVal <= following.val)
            if ordinary or wrap:
                break
            current = following
            if current is head:
                break
        inserted.next = current.next
        current.next = inserted
        return head
