class Solution:
    def longestStrChain(self, words):
        best = {}
        answer = 1
        for word in sorted(words, key=len):
            longest = 1
            for index in range(len(word)):
                predecessor = word[:index] + word[index + 1:]
                longest = max(longest, best.get(predecessor, 0) + 1)
            best[word] = longest
            answer = max(answer, longest)
        return answer
