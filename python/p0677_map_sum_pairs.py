class _Node:
    def __init__(self):
        self.children = {}
        self.total = 0


class MapSum:
    def __init__(self):
        self.values = {}
        self.root = _Node()

    def insert(self, key, val):
        delta = val - self.values.get(key, 0)
        self.values[key] = val
        node = self.root
        node.total += delta
        for char in key:
            child = node.children.get(char)
            if child is None:
                child = _Node()
                node.children[char] = child
            node = child
            node.total += delta

    def sum(self, prefix):
        node = self.root
        for char in prefix:
            node = node.children.get(char)
            if node is None:
                return 0
        return node.total
