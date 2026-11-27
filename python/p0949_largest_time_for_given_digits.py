from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, arr):
        best = -1
        for first,second,third,fourth in permutations(arr):
            hour = 10 * first + second
            minute = 10 * third + fourth
            if hour < 24 and minute < 60:
                best = max(best,60 * hour + minute)
        if best < 0:
            return ''
        return f'{best // 60:02d}:{best % 60:02d}'
