class Solution:
    def splitListToParts(self, head, k):
        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next
        base, extra = divmod(length, k)
        parts = []
        node = head
        for part in range(k):
            parts.append(node)
            size = base + (part < extra)
            if size:
                for _ in range(size - 1):
                    node = node.next
                following = node.next
                node.next = None
                node = following
        return parts
