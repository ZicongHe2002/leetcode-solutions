from collections import deque


class MinStack:
    def __init__(self):
        self._entries = deque()

    def push(self, val):
        smallest = min(val, self._entries[-1][1]) if self._entries else val
        self._entries.append((val, smallest))

    def pop(self):
        self._entries.pop()

    def top(self):
        return self._entries[-1][0]

    def getMin(self):
        return self._entries[-1][1]
