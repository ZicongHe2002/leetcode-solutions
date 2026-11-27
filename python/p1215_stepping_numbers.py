from collections import deque


class Solution:
    def countSteppingNumbers(self, low, high):
        answer = [0] if low == 0 else []
        pending = deque(range(1, 10))
        while pending:
            value = pending.popleft()
            if value > high:
                continue
            if value >= low:
                answer.append(value)
            digit = value % 10
            if digit > 0:
                following = value * 10 + digit - 1
                if following <= high:
                    pending.append(following)
            if digit < 9:
                following = value * 10 + digit + 1
                if following <= high:
                    pending.append(following)
        return answer
