class Solution:
    def maxProduct(self, words):
        encoded = []
        for word in words:
            mask = 0
            for letter in word:
                mask |= 1 << (ord(letter) - ord('a'))
            encoded.append((mask, len(word)))

        best = 0
        for left in range(len(encoded)):
            left_mask, left_length = encoded[left]
            for right in range(left + 1, len(encoded)):
                right_mask, right_length = encoded[right]
                if left_mask & right_mask == 0:
                    best = max(best, left_length * right_length)
        return best
