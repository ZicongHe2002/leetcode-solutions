class Solution:
    def reverseParentheses(self, s):
        matching = {}
        pending = []
        for index, letter in enumerate(s):
            if letter == '(':
                pending.append(index)
            elif letter == ')':
                opening = pending.pop()
                matching[index] = opening
                matching[opening] = index
        answer = []
        index, direction = 0, 1
        while 0 <= index < len(s):
            if s[index] in '()':
                index = matching[index]
                direction = -direction
            else:
                answer.append(s[index])
            index += direction
        return ''.join(answer)
