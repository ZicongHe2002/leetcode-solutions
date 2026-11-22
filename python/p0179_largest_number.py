from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        def compare(first, second):
            forward, backward = first + second, second + first
            return (backward > forward) - (backward < forward)

        parts = sorted(map(str, nums), key=cmp_to_key(compare))
        return ''.join(parts).lstrip('0') or '0'
