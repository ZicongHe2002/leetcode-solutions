class Solution:
    def titleToNumber(self, columnTitle):
        number = 0
        for letter in columnTitle:
            number = number * 26 + ord(letter) - ord('A') + 1
        return number
