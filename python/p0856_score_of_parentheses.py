class Solution:
    def scoreOfParentheses(self, s):
        depth = score = 0
        for index, letter in enumerate(s):
            if letter == '(':
                depth += 1
            else:
                depth -= 1
                if s[index - 1] == '(':
                    score += 1 << depth
        return score
