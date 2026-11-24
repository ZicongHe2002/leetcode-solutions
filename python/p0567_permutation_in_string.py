class Solution:
    def checkInclusion(self, s1, s2):
        if not s1:
            return True
        if len(s1) > len(s2):
            return False
        balance = [0] * 26
        for character in s1:
            balance[ord(character) - ord('a')] += 1
        missing = len(s1)
        for right, character in enumerate(s2):
            index = ord(character) - ord('a')
            if balance[index] > 0:
                missing -= 1
            balance[index] -= 1
            if right >= len(s1):
                previous = ord(s2[right - len(s1)]) - ord('a')
                balance[previous] += 1
                if balance[previous] > 0:
                    missing += 1
            if missing == 0:
                return True
        return False
