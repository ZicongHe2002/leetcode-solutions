class Solution:
    def bestRotation(self, nums):
        size = len(nums)
        changes = [0] * size
        for index,value in enumerate(nums):
            if value == 0:
                continue
            start = (index - value + 1) % size
            end = (index + 1) % size
            changes[start] += 1
            changes[end] -= 1
            if start > end:
                changes[0] += 1
        bad = 0
        best_bad = size + 1
        best = 0
        for rotation,change in enumerate(changes):
            bad += change
            if bad < best_bad:
                best_bad = bad
                best = rotation
        return best
