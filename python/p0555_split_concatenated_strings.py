class Solution:
    def splitLoopedString(self, strs):
        oriented = [max(word, word[::-1]) for word in strs]
        joined = ''.join(oriented)
        answer = ''
        offset = 0
        for word in strs:
            middle = joined[offset + len(word):] + joined[:offset]
            for cut_word in (word, word[::-1]):
                for cut in range(len(cut_word)):
                    candidate = cut_word[cut:] + middle + cut_word[:cut]
                    answer = max(answer, candidate)
            offset += len(word)
        return answer
