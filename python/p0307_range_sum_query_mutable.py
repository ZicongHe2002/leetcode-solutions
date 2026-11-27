class NumArray:
    def __init__(self, nums):
        self._values = nums[:]
        self._tree = [0] + nums[:]
        for index in range(1, len(self._tree)):
            parent = index + (index & -index)
            if parent < len(self._tree):
                self._tree[parent] += self._tree[index]

    def update(self, index, val):
        difference = val - self._values[index]
        self._values[index] = val
        index += 1
        while index < len(self._tree):
            self._tree[index] += difference
            index += index & -index

    def _prefix_sum(self, stop):
        total = 0
        while stop:
            total += self._tree[stop]
            stop -= stop & -stop
        return total

    def sumRange(self, left, right):
        return self._prefix_sum(right + 1) - self._prefix_sum(left)
