class MyHashMap:
    def __init__(self):
        self._buckets = [[] for _ in range(1009)]

    def put(self, key, value):
        bucket = self._buckets[key % len(self._buckets)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        for candidate, value in self._buckets[key % len(self._buckets)]:
            if candidate == key:
                return value
        return -1

    def remove(self, key):
        bucket = self._buckets[key % len(self._buckets)]
        for index, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(index)
                return
