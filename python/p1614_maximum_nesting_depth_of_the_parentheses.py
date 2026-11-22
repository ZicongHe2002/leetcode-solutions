class Solution:
    def maxDepth(self, s):
        depth = best = 0
        for letter in s:
            if letter == '(':
                depth += 1
                best = max(best, depth)
            elif letter == ')':
                depth -= 1
        return best
