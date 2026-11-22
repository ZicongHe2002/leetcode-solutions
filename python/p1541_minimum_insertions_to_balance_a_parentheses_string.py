class Solution:
    def minInsertions(self, s):
        inserted = needed = 0
        for letter in s:
            if letter == '(':
                if needed % 2:
                    inserted += 1
                    needed -= 1
                needed += 2
            else:
                needed -= 1
                if needed < 0:
                    inserted += 1
                    needed = 1
        return inserted + needed
