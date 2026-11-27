class Solution:
    def findAndReplacePattern(self, words, pattern):
        def signature(text):
            identifiers = {}
            return tuple(identifiers.setdefault(char,len(identifiers)) for char in text)

        expected = signature(pattern)
        return [word for word in words if signature(word) == expected]
