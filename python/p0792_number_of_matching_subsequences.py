from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s, words):
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append((word,0))
        matched = 0
        for char in s:
            current = waiting.pop(char,[])
            for word,index in current:
                index += 1
                if index == len(word):
                    matched += 1
                else:
                    waiting[word[index]].append((word,index))
        return matched
