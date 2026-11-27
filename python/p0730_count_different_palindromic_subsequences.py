class Solution:
    def countPalindromicSubsequences(self, s):
        length, modulus = len(s), 10**9 + 7
        previous, following = [-1] * length, [length] * length
        last = {}
        for index, char in enumerate(s):
            previous[index] = last.get(char, -1)
            last[char] = index
        last = {}
        for index in range(length - 1, -1, -1):
            following[index] = last.get(s[index], length)
            last[s[index]] = index
        counts = [[0] * length for _ in range(length)]
        for left in range(length - 1, -1, -1):
            counts[left][left] = 1
            for right in range(left + 1, length):
                inner = counts[left + 1][right - 1]
                if s[left] != s[right]:
                    value = counts[left + 1][right] + counts[left][right - 1] - inner
                else:
                    first, final = following[left], previous[right]
                    if first > final:
                        value = 2 * inner + 2
                    elif first == final:
                        value = 2 * inner + 1
                    else:
                        value = 2 * inner - counts[first + 1][final - 1]
                counts[left][right] = value % modulus
        return counts[0][-1]
