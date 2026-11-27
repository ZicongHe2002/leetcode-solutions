from collections import Counter


class Solution:
    def countCharacters(self, words, chars):
        available = Counter(chars)
        answer = 0
        for word in words:
            needed = Counter(word)
            if all(count <= available[letter] for letter, count in needed.items()):
                answer += len(word)
        return answer
