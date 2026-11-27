from random import getrandbits


class _Node:
    def __init__(self, value, height):
        self.value = value
        self.next = [None] * height


class Skiplist:
    def __init__(self):
        self.levels = 32
        self.head = _Node(float('-inf'), self.levels)

    def predecessors(self, target):
        result = [None] * self.levels
        node = self.head
        for level in range(self.levels - 1, -1, -1):
            while node.next[level] is not None and node.next[level].value < target:
                node = node.next[level]
            result[level] = node
        return result

    def search(self, target):
        following = self.predecessors(target)[0].next[0]
        return following is not None and following.value == target

    def add(self, num):
        previous = self.predecessors(num)
        height = 1
        while height < self.levels and getrandbits(1):
            height += 1
        node = _Node(num, height)
        for level in range(height):
            node.next[level] = previous[level].next[level]
            previous[level].next[level] = node

    def erase(self, num):
        previous = self.predecessors(num)
        node = previous[0].next[0]
        if node is None or node.value != num:
            return False
        for level in range(self.levels):
            if previous[level].next[level] is node:
                previous[level].next[level] = node.next[level]
        return True
