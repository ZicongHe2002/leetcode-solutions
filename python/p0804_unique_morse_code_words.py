class Solution:
    def uniqueMorseRepresentations(self, words):
        codes = ('.-','-...','-.-.','-..','.','..-.','--.','....','..','.---',
                 '-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-',
                 '..-','...-','.--','-..-','-.--','--..')
        encoded = {''.join(codes[ord(char) - ord('a')] for char in word) for word in words}
        return len(encoded)
