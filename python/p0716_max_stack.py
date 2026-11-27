class _Node:
    def __init__(self, value, sequence):
        self.value = value
        self.key = (value, sequence)
        self.left = self.right = None
        self.previous = self.next = None
        self.height = 1


def _height(node):
    return node.height if node is not None else 0


def _update(node):
    node.height = 1 + max(_height(node.left), _height(node.right))


def _rotate_left(node):
    root = node.right
    node.right = root.left
    root.left = node
    _update(node)
    _update(root)
    return root


def _rotate_right(node):
    root = node.left
    node.left = root.right
    root.right = node
    _update(node)
    _update(root)
    return root


def _balance(node):
    _update(node)
    difference = _height(node.left) - _height(node.right)
    if difference > 1:
        if _height(node.left.left) < _height(node.left.right):
            node.left = _rotate_left(node.left)
        return _rotate_right(node)
    if difference < -1:
        if _height(node.right.right) < _height(node.right.left):
            node.right = _rotate_right(node.right)
        return _rotate_left(node)
    return node


def _insert(root, node):
    if root is None:
        return node
    if node.key < root.key:
        root.left = _insert(root.left, node)
    else:
        root.right = _insert(root.right, node)
    return _balance(root)


def _detach_min(root):
    if root.left is None:
        return root.right, root
    root.left, minimum = _detach_min(root.left)
    return _balance(root), minimum


def _delete(root, key):
    if key < root.key:
        root.left = _delete(root.left, key)
    elif key > root.key:
        root.right = _delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        right, successor = _detach_min(root.right)
        successor.left, successor.right = root.left, right
        return _balance(successor)
    return _balance(root)


class MaxStack:
    def __init__(self):
        self.root = self.tail = None
        self.sequence = 0

    def push(self, x):
        node = _Node(x, self.sequence)
        self.sequence += 1
        node.previous = self.tail
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        self.root = _insert(self.root, node)

    def _remove(self, node):
        self.root = _delete(self.root, node.key)
        if node.previous is not None:
            node.previous.next = node.next
        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous
        node.left = node.right = node.previous = node.next = None
        return node.value

    def pop(self):
        return self._remove(self.tail)

    def top(self):
        return self.tail.value

    def _maximum(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node

    def peekMax(self):
        return self._maximum().value

    def popMax(self):
        return self._remove(self._maximum())
