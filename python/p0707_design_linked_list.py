class _Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self._head = _Node()
        self._tail = self._head
        self._size = 0

    def _before(self, index):
        node = self._head
        for _ in range(index):
            node = node.next
        return node

    def _insert_after(self, previous, val):
        node = _Node(val, previous.next)
        previous.next = node
        if self._tail is previous:
            self._tail = node
        self._size += 1

    def get(self, index):
        if index >= self._size:
            return -1
        return self._before(index).next.val

    def addAtHead(self, val):
        self._insert_after(self._head, val)

    def addAtTail(self, val):
        self._insert_after(self._tail, val)

    def addAtIndex(self, index, val):
        if index <= self._size:
            self._insert_after(self._before(index), val)

    def deleteAtIndex(self, index):
        if index >= self._size:
            return
        previous = self._before(index)
        removed = previous.next
        previous.next = removed.next
        if self._tail is removed:
            self._tail = previous
        self._size -= 1
