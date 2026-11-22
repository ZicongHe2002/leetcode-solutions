class Solution:
    @staticmethod
    def _fold(character):
        if 'A' <= character <= 'Z':
            return character.lower()
        if 'a' <= character <= 'z' or '0' <= character <= '9':
            return character
        return None

    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            first, last = self._fold(s[left]), self._fold(s[right])
            if first is None:
                left += 1
                continue
            if last is None:
                right -= 1
                continue
            if first != last:
                return False
            left += 1
            right -= 1
        return True
