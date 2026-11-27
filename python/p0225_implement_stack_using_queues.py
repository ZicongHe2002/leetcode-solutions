from collections import deque


class MyStack:
    def __init__(self):
        self._queue = deque()

    def push(self, x):
        self._queue.append(x)
        for _ in range(len(self._queue) - 1):
            self._queue.append(self._queue.popleft())

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not self._queue
