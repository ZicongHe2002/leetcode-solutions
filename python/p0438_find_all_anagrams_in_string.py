class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        needed = [0] * 26
        window = [0] * 26
        for character in p:
            needed[ord(character) - ord('a')] += 1
        result = []
        for right, character in enumerate(s):
            window[ord(character) - ord('a')] += 1
            if right >= len(p):
                window[ord(s[right - len(p)]) - ord('a')] -= 1
            if right + 1 >= len(p) and window == needed:
                result.append(right - len(p) + 1)
        return result
