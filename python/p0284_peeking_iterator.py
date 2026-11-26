class PeekingIterator:
    def __init__(self, iterator):
        self._iterator = iterator
        self._has_value = iterator.hasNext()
        self._value = iterator.next() if self._has_value else None

    def peek(self):
        return self._value

    def next(self):
        value = self._value
        self._has_value = self._iterator.hasNext()
        self._value = self._iterator.next() if self._has_value else None
        return value

    def hasNext(self):
        return self._has_value
