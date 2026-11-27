class Solution:
    def removeVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return ''.join(letter for letter in s if letter not in vowels)
