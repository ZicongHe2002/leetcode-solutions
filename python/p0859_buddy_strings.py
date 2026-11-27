class Solution:
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        mismatches = []
        for index, (left, right) in enumerate(zip(s, goal)):
            if left != right:
                mismatches.append(index)
                if len(mismatches) > 2:
                    return False
        if not mismatches:
            return len(set(s)) < len(s)
        if len(mismatches) != 2:
            return False
        first, second = mismatches
        return s[first] == goal[second] and s[second] == goal[first]
