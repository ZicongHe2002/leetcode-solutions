class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        first = strs[0]
        for index, character in enumerate(first):
            for word in strs:
                if index == len(word) or word[index] != character:
                    return first[:index]
        return first
