class Solution:
    def numSpecialEquivGroups(self, words):
        signatures = {(''.join(sorted(word[::2])),''.join(sorted(word[1::2]))) for word in words}
        return len(signatures)
