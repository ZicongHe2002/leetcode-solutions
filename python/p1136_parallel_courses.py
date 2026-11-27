from collections import deque


class Solution:
    def minimumSemesters(self, n, relations):
        following = [[] for _ in range(n + 1)]
        prerequisites = [0] * (n + 1)
        for first, second in relations:
            following[first].append(second)
            prerequisites[second] += 1
        pending = deque(course for course in range(1, n + 1) if prerequisites[course] == 0)
        semesters = completed = 0
        while pending:
            semesters += 1
            for _ in range(len(pending)):
                course = pending.popleft()
                completed += 1
                for other in following[course]:
                    prerequisites[other] -= 1
                    if prerequisites[other] == 0:
                        pending.append(other)
        return semesters if completed == n else -1
