class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        forward, backward = {}, {}
        for character, word in zip(pattern, words):
            if character in forward and forward[character] != word:
                return False
            if word in backward and backward[word] != character:
                return False
            forward[character] = word
            backward[word] = character
        return True
