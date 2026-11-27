class Solution:
    def findRepeatedDnaSequences(self, s):
        codes = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        mask = (1 << 20) - 1
        encoded = 0
        seen = set()
        repeated = set()
        for index, character in enumerate(s):
            encoded = ((encoded << 2) | codes[character]) & mask
            if index < 9:
                continue
            if encoded in seen:
                repeated.add(s[index - 9:index + 1])
            else:
                seen.add(encoded)
        return list(repeated)
