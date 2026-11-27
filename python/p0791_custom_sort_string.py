from collections import Counter


class Solution:
    def customSortString(self, order, s):
        counts = Counter(s)
        parts = [char * counts.pop(char,0) for char in order]
        parts.extend(char * count for char,count in counts.items())
        return ''.join(parts)
