class Solution:
    def longestValidParentheses(self, s):
        positions = [-1]
        longest = 0
        for index, character in enumerate(s):
            if character == '(':
                positions.append(index)
            else:
                positions.pop()
                if not positions:
                    positions.append(index)
                else:
                    longest = max(longest, index - positions[-1])
        return longest
