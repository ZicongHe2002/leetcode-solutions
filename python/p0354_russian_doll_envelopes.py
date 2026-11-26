from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes):
        ordered = sorted(envelopes, key=lambda item: (item[0], -item[1]))
        tails = []
        for _, height in ordered:
            position = bisect_left(tails, height)
            if position == len(tails):
                tails.append(height)
            else:
                tails[position] = height
        return len(tails)
