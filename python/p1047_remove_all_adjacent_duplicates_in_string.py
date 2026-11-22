class Solution:
    def removeDuplicates(self, s):
        remaining = []
        for letter in s:
            if remaining and remaining[-1] == letter:
                remaining.pop()
            else:
                remaining.append(letter)
        return ''.join(remaining)
