class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            groups.setdefault(tuple(counts), []).append(word)
        return list(groups.values())
