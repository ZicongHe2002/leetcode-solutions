from bisect import bisect_left, bisect_right
from collections import defaultdict


class MajorityChecker:
    @staticmethod
    def merge(first, second):
        left, left_count = first
        right, right_count = second
        if left_count == 0:
            return second
        if right_count == 0:
            return first
        if left == right:
            return left, left_count + right_count
        if left_count >= right_count:
            return left, left_count - right_count
        return right, right_count - left_count

    def __init__(self, arr):
        self.positions = defaultdict(list)
        self.size = 1
        while self.size < len(arr):
            self.size *= 2
        self.tree = [(None, 0)] * (2 * self.size)
        for index, value in enumerate(arr):
            self.positions[value].append(index)
            self.tree[self.size + index] = (value, 1)
        for index in range(self.size - 1, 0, -1):
            self.tree[index] = self.merge(self.tree[2 * index], self.tree[2 * index + 1])

    def query(self, left, right, threshold):
        begin, end = left + self.size, right + self.size + 1
        result = (None, 0)
        while begin < end:
            if begin % 2:
                result = self.merge(result, self.tree[begin])
                begin += 1
            if end % 2:
                end -= 1
                result = self.merge(result, self.tree[end])
            begin //= 2
            end //= 2
        candidate = result[0]
        if candidate is None:
            return -1
        positions = self.positions[candidate]
        count = bisect_right(positions, right) - bisect_left(positions, left)
        return candidate if count >= threshold else -1
