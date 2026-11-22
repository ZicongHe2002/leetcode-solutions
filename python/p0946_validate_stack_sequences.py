class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        next_pop = 0
        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[next_pop]:
                stack.pop()
                next_pop += 1
        return next_pop == len(popped)
