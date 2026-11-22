class Solution:
    def findContentChildren(self, g, s):
        needs, cookies = sorted(g), sorted(s)
        satisfied = 0
        for cookie in cookies:
            if satisfied < len(needs) and cookie >= needs[satisfied]:
                satisfied += 1
        return satisfied
