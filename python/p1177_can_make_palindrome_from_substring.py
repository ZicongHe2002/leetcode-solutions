class Solution:
    def canMakePaliQueries(self, s, queries):
        prefix = [0]
        for letter in s:
            prefix.append(prefix[-1] ^ (1 << (ord(letter) - ord('a'))))
        return [((prefix[right + 1] ^ prefix[left]).bit_count() // 2 <= replacements)
                for left, right, replacements in queries]
