class Solution:
    def findLUSlength(self, strs):
        ordered = sorted(strs, key=len, reverse=True)

        def is_subsequence(candidate, other):
            matched = 0
            for char in other:
                if matched < len(candidate) and candidate[matched] == char:
                    matched += 1
            return matched == len(candidate)

        for index, candidate in enumerate(ordered):
            if all(index == other_index or len(other) < len(candidate) or
                   not is_subsequence(candidate, other)
                   for other_index, other in enumerate(ordered)):
                return len(candidate)
        return -1
