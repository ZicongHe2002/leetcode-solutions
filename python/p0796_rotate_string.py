class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        size = len(s)
        prefix = [0] * size
        matched = 0
        for index in range(1, size):
            while matched and goal[index] != goal[matched]:
                matched = prefix[matched - 1]
            if goal[index] == goal[matched]:
                matched += 1
            prefix[index] = matched
        matched = 0
        for index in range(2 * size - 1):
            character = s[index % size]
            while matched and character != goal[matched]:
                matched = prefix[matched - 1]
            if character == goal[matched]:
                matched += 1
            if matched == size:
                return True
        return False
