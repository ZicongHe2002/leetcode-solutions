class MyHashSet:
    def __init__(self):
        self._buckets = [[] for _ in range(1009)]

    def add(self, key):
        bucket = self._buckets[key % len(self._buckets)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key):
        bucket = self._buckets[key % len(self._buckets)]
        for index, candidate in enumerate(bucket):
            if candidate == key:
                bucket.pop(index)
                return

    def contains(self, key):
        return key in self._buckets[key % len(self._buckets)]
