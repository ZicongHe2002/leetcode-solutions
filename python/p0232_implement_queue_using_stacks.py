class MyQueue:
    def __init__(self):
        self._incoming = []
        self._outgoing = []

    def _fill_outgoing(self):
        if not self._outgoing:
            while self._incoming:
                self._outgoing.append(self._incoming.pop())

    def push(self, x):
        self._incoming.append(x)

    def pop(self):
        self._fill_outgoing()
        return self._outgoing.pop()

    def peek(self):
        self._fill_outgoing()
        return self._outgoing[-1]

    def empty(self):
        return not self._incoming and not self._outgoing
