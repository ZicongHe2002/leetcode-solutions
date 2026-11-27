from collections import Counter


class Solution:
    def wordSubsets(self, words1, words2):
        required = Counter()
        for word in words2:
            required |= Counter(word)
        answer = []
        for word in words1:
            available = Counter(word)
            if all(available[char] >= count for char,count in required.items()):
                answer.append(word)
        return answer
