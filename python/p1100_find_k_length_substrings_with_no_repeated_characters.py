class Solution:
    def numKLenSubstrNoRepeats(self, s, k):
        frequencies = {}
        answer = 0
        for right, letter in enumerate(s):
            frequencies[letter] = frequencies.get(letter, 0) + 1
            if right >= k:
                outgoing = s[right - k]
                frequencies[outgoing] -= 1
                if frequencies[outgoing] == 0:
                    del frequencies[outgoing]
            if right + 1 >= k and len(frequencies) == k:
                answer += 1
        return answer
