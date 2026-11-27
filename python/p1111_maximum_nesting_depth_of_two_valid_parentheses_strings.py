class Solution:
    def maxDepthAfterSplit(self, seq):
        answer = []
        depth = 0
        for bracket in seq:
            if bracket == '(':
                depth += 1
                answer.append(depth % 2)
            else:
                answer.append(depth % 2)
                depth -= 1
        return answer
