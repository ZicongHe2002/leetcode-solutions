class MyCircularQueue:
    def __init__(self, k):
        self._data = [0] * k
        self._front = 0
        self._size = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        self._data[(self._front + self._size) % len(self._data)] = value
        self._size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self._data[self._front]

    def Rear(self):
        return (-1 if self.isEmpty()
                else self._data[(self._front + self._size - 1) % len(self._data)])

    def isEmpty(self):
        return self._size == 0

    def isFull(self):
        return self._size == len(self._data)
