class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        previous_two = 1
        previous_one = 0 if s[0] == '0' else 1
        for index in range(1, len(s)):
            ways = previous_one if s[index] != '0' else 0
            if 10 <= int(s[index - 1:index + 1]) <= 26:
                ways += previous_two
            previous_two, previous_one = previous_one, ways
        return previous_one
