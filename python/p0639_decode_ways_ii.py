class Solution:
    def numDecodings(self, s):
        modulus = 10**9 + 7
        earlier = previous = 1
        for index, char in enumerate(s):
            single = 9 if char == '*' else int(char != '0')
            pair = 0
            if index:
                left = s[index - 1]
                if char == '*':
                    if left == '*':
                        pair = 15
                    elif left == '1':
                        pair = 9
                    elif left == '2':
                        pair = 6
                elif left == '*':
                    pair = 2 if char <= '6' else 1
                elif left != '0' and 10 <= int(left + char) <= 26:
                    pair = 1
            current = (previous * single + earlier * pair) % modulus
            earlier, previous = previous, current
        return previous
