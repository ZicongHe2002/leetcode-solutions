from collections import deque


class Solution:
    def openLock(self, deadends, target):
        seen = set(deadends)
        if '0000' in seen:
            return -1
        seen.add('0000')
        queue = deque([('0000', 0)])
        while queue:
            state, turns = queue.popleft()
            if state == target:
                return turns
            for index, digit in enumerate(state):
                for change in (-1, 1):
                    following = state[:index] + str((int(digit) + change) % 10) + state[index + 1:]
                    if following not in seen:
                        seen.add(following)
                        queue.append((following, turns + 1))
        return -1
