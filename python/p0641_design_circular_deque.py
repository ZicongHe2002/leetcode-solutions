class MyCircularDeque:
    def __init__(self, k):
        self._data = [0] * k
        self._front = 0
        self._size = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = value
        self._size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self._data[(self._front + self._size) % len(self._data)] = value
        self._size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self._size -= 1
        return True

    def getFront(self):
        return -1 if self.isEmpty() else self._data[self._front]

    def getRear(self):
        return (-1 if self.isEmpty()
                else self._data[(self._front + self._size - 1) % len(self._data)])

    def isEmpty(self):
        return self._size == 0

    def isFull(self):
        return self._size == len(self._data)
