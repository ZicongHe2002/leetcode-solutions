from collections import Counter


class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False
        remaining = Counter(hand)
        for start in sorted(remaining):
            groups = remaining[start]
            if not groups:
                continue
            for value in range(start, start + groupSize):
                if remaining[value] < groups:
                    return False
                remaining[value] -= groups
        return True
