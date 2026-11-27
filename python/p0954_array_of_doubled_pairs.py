from collections import Counter


class Solution:
    def canReorderDoubled(self, arr):
        counts = Counter(arr)
        for value in sorted(counts,key=abs):
            amount = counts[value]
            if amount == 0:
                continue
            if value == 0:
                if amount % 2:
                    return False
                counts[value] = 0
                continue
            if counts[2 * value] < amount:
                return False
            counts[2 * value] -= amount
            counts[value] = 0
        return True
