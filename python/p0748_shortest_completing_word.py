from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        needed = Counter(char.lower() for char in licensePlate if char.isalpha())
        best = None
        for word in words:
            if best is not None and len(word) >= len(best):
                continue
            available = Counter(word)
            if all(available[char] >= count for char, count in needed.items()):
                best = word
        return best
