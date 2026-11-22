class _Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.previous = None
        self.following = None


class LRUCache:
    def __init__(self, capacity):
        self._capacity = capacity
        self._nodes = {}
        self._oldest = _Node()
        self._latest = _Node()
        self._oldest.following = self._latest
        self._latest.previous = self._oldest

    def _unlink(self, node):
        node.previous.following = node.following
        node.following.previous = node.previous

    def _append_latest(self, node):
        node.previous = self._latest.previous
        node.following = self._latest
        self._latest.previous.following = node
        self._latest.previous = node

    def get(self, key):
        node = self._nodes.get(key)
        if node is None:
            return -1
        self._unlink(node)
        self._append_latest(node)
        return node.value

    def put(self, key, value):
        node = self._nodes.get(key)
        if node is not None:
            node.value = value
            self._unlink(node)
            self._append_latest(node)
            return
        node = _Node(key, value)
        self._nodes[key] = node
        self._append_latest(node)
        if len(self._nodes) > self._capacity:
            evicted = self._oldest.following
            self._unlink(evicted)
            del self._nodes[evicted.key]
