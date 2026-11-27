from bisect import bisect_right


class SnapshotArray:
    def __init__(self, length):
        self.history = [[(-1, 0)] for _ in range(length)]
        self.current = 0

    def set(self, index, val):
        versions = self.history[index]
        if versions[-1][0] == self.current:
            versions[-1] = (self.current, val)
        else:
            versions.append((self.current, val))

    def snap(self):
        self.current += 1
        return self.current - 1

    def get(self, index, snap_id):
        versions = self.history[index]
        position = bisect_right(versions, (snap_id, float('inf'))) - 1
        return versions[position][1]
