from collections import OrderedDict


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.entries = {}
        self.buckets = {}
        self.minimum = 0

    def _touch(self, key, value):
        _, frequency = self.entries[key]
        bucket = self.buckets[frequency]
        del bucket[key]
        if not bucket:
            del self.buckets[frequency]
            if self.minimum == frequency:
                self.minimum += 1
        self.entries[key] = (value, frequency + 1)
        self.buckets.setdefault(frequency + 1, OrderedDict())[key] = None

    def get(self, key):
        if key not in self.entries:
            return -1
        value, _ = self.entries[key]
        self._touch(key, value)
        return value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.entries:
            self._touch(key, value)
            return
        if len(self.entries) == self.capacity:
            bucket = self.buckets[self.minimum]
            removed, _ = bucket.popitem(last=False)
            del self.entries[removed]
            if not bucket:
                del self.buckets[self.minimum]
        self.entries[key] = (value, 1)
        self.buckets.setdefault(1, OrderedDict())[key] = None
        self.minimum = 1
