from collections import Counter


class Solution:
    def findSubstring(self, s, words):
        if not words:
            return []
        width = len(words[0])
        total = width * len(words)
        if len(s) < total:
            return []
        required = Counter(words)
        result = []
        for offset in range(width):
            left = offset
            used = 0
            counts = {}
            for right in range(offset, len(s) - width + 1, width):
                word = s[right:right + width]
                if word not in required:
                    counts.clear()
                    used = 0
                    left = right + width
                    continue
                counts[word] = counts.get(word, 0) + 1
                used += 1
                while counts[word] > required[word]:
                    removed = s[left:left + width]
                    counts[removed] -= 1
                    used -= 1
                    left += width
                if used == len(words):
                    result.append(left)
                    removed = s[left:left + width]
                    counts[removed] -= 1
                    used -= 1
                    left += width
        return result
