from bisect import bisect_right
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key, value, timestamp):
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key, timestamp):
        times = self.timestamps.get(key,[])
        position = bisect_right(times,timestamp) - 1
        return self.values[key][position] if position >= 0 else ''
