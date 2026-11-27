class Solution:
    def findLongestChain(self, pairs):
        previous_end = -1001
        longest = 0
        for left, right in sorted(pairs, key=lambda pair: pair[1]):
            if left > previous_end:
                longest += 1
                previous_end = right
        return longest
